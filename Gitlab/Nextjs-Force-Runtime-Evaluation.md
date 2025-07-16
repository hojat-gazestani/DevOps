# Build-Time vs. Runtime Variables

## Explain the problem
- I have three backend server with different URLs defined in Gitlab environment variable and trying to build docker container once and use multiple time on `dev`, `stage` and `prod` environment.
- but my problem was Nextjs only recogonize variable during the build time not runtime, So I solve the problem as explain in the follwoing.

- This is my Gitlab pipeline and I extended the run stage but I have different variable for each one.

```sh
vim .gitlab-ci.yml
stages:
  - build
  - run

build:
  stage: build
  variables:
    IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
    NEXT_PUBLIC_BACKEND_IP: "192.168.1.1"
    BACKEND_IP: "192.168.1.1"
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -f docker/Dockerfile -t $IMAGE_TAG .
    - docker push $IMAGE_TAG
  only:
    - stage
  tags:
    - gitlab-docker

.run:
  stage: run
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - echo "$ENVS" > docker/.env
    - docker compose -p ${PROJ} -f docker/docker-compose.yml up -d
  only:
    - stage

run-dev:
  extends: .run
  environment: dev
  when: manual
  tags:
    - dev

run-stage:
  extends: .run
  environment: stage
  when: manual
  tags:
    - stage

run-prod:
  extends: .run
  environment: prod
  when: manual
  tags:
    - prod
```

```sh
vim docker/docker-compose.yml
---
services:
  tala-be:
    image: $CI_REGISTRY_IMAGE:latest
    pull_policy: always
    container_name: fron-${PROJ}
    restart: always
    ports:
      - "${LPORT}:3000"
    env_file:
      - .env

```

## Build-Time

### Creating the nextjs simple application

```sh
npx create-next-app@latest my-simple-app
cd my-simple-app/
vim src/app/page.tsx
```

```tsx
export const dynamic = 'force-dynamic';

import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <p className="text-lg font-semibold">
          I am connected to backend server with IP: {process.env.NEXT_PUBLIC_BACKEND_IP}
        </p>
        <p className="text-lg font-semibold">
          I am connected to backend server with IP: {process.env.BACKEND_IP}
        </p>
...
```

```sh
export BACKEND_IP="192.168.1.1"
export NEXT_PUBLIC_BACKEND_IP="192.168.1.1"

npm run dev
```

### Dockerizing the project
```sh
mkdir docker
vim docker/Dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package*.json ./
RUN npm install --omit=dev
ENV NODE_ENV production
EXPOSE 3000
CMD ["npm", "start"]
```

### Build the Docker Image

```sh
docker build -f docker/Dockerfile -t my-nextjs-app --no-cache .
docker run -p 80:3000 -e NEXT_PUBLIC_BACKEND_IP="1.1.1.1" -e BACKEND_IP="1.1.1.1" my-nextjs-app
```

## Runtime Variables 

- `NEXT_PUBLIC_` variables are available at build time for static site generation (SSG) or client-side rendering. And the variable provided at runtime via `docker run -e`, are not included in the built JavaScript bundle. To ensure `NEXT_PUBLIC_BACKEND_IP` and `BACKEND_IP` are correctly passed and rendered,Force Runtime Evaluation.

- Next.js is statically generating the page, which means environment variables are embedded at build time. To make `NEXT_PUBLIC_BACKEND_IP` and `BACKEND_IP` available at runtime:

- **Disable Static Generation:** Ensure the page is server-rendered (SSR) or client-rendered (CSR) so it can access runtime environment variables.
- Add dynamic to page.tsx to force dynamic rendering:

```tsx
export const dynamic = 'force-dynamic';

import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <p className="text-lg font-semibold">
          I am connected to backend server with IP: {process.env.NEXT_PUBLIC_BACKEND_IP}
        </p>
        <p className="text-lg font-semibold">
          I am connected to backend server with IP: {process.env.BACKEND_IP}
        </p>
...
```

- The `dynamic = 'force-dynamic'` ensures the page is rendered on the server for each request, allowing runtime environment variables to be used.

### Rebuild the Docker Image

```sh
docker build -f docker/Dockerfile -t my-nextjs-app --no-cache .
```

### Test the Application

```sh
docker run -p 80:3000 -e NEXT_PUBLIC_BACKEND_IP="1.1.1.1" -e BACKEND_IP="1.1.1.1" my-nextjs-app
```