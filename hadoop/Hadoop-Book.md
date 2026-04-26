# Hadoop



## Main Problem
Storage capacity has grown much faster than disk speed.
Modern disks can store huge amounts of data, but **reading and writing data is slow** if you use only one disk. As data sizes reach terabytes and beyond, processing data on a single machine becomes impractical.



### Key Ideas Explained

1. Disk speed is the bottleneck

   + Old disks (1990) were small but could be read quickly end-to-end.

   + Modern disks are very large (1 TB+) but take hours to read completely.

   + Writing data is even slower than reading.

2. Parallelism is the solution

   + Instead of one large disk, use **many disks in parallel.**

   + If data is spread across 100 disks, it can be read **100× faster.**

   + This reduces analysis time from hours to minutes.

3. Sharing disks is efficient

   + Using many disks is not wasteful if multiple datasets and users share them.

   + Jobs usually run at different times, so users benefit from faster performance.

4. Hardware failures are unavoidable

   + With many machines, **failures are normal,** not exceptional.

   + The solution is **replication**: storing multiple copies of data.

   + Hadoop’s filesystem (**HDFS**) handles this automatically.

5. Combining distributed data is hard

   + Analysis often needs data from many disks to be combined.

   + Doing this correctly in distributed systems is complex.

6. MapReduce simplifies analysis

   + MapReduce hides the complexity of distributed reads, writes, and failures.

   + It splits work into **map** and **reduce** phases.

   + The framework handles data movement and reliability.



### Bottom Line
> Hadoop solves two big problems at once:
>
> + How to store massive data reliably across many machines (HDFS)
>
> + How to analyze that data efficiently in parallel (MapReduce)

Because Hadoop uses **cheap hardware** and is **open source**, it provides a **scalable**, **reliable**, and **affordable** platform for big data storage and analysis.



### Main Idea

**MapReduce enables querying all your data, not just small samples.**
Although it may seem inefficient to scan large datasets for each query, this **batch-processing approach is actually its strength.**



### Key Points Explained

1. MapReduce is a batch query system

   + It processes **large portions or the entirety of a dataset** for each query.

   + This is different from traditional databases that rely heavily on <u>indexes</u> and <u>small</u>, <u>selective queries</u>.

2. Ad hoc queries become practical

   + You can ask **new, unplanned questions** and get answers in a reasonable time.

   + There is no need to design schemas or indexes in advance for every possible question.

3. Unlocks previously unused data

   + Data that was too large or slow to analyze (e.g., archived on tape or disk) becomes usable.

   + Organizations can now extract value from historical data.

4. Changes how people think about data

   + Instead of asking “What can we afford to query?”, people ask “What can we learn from all our data?”

   + Faster answers lead to new questions and deeper insights.

5. Real-world example (Rackspace / Mailtrust)

   + Hadoop was used to analyze **hundreds of gigabytes of email logs**.

   + An ad hoc query revealed the **geographic distribution of users**.

   + The insight was so valuable that it became a **regular monthly job.**

   + The results directly influenced **where new data centers were built**, improving customer service.



> Bottom Line
>
> **The power of MapReduce lies in making full-dataset analysis feasible.**
> By enabling fast, ad hoc queries over massive data volumes, Hadoop helps organizations discover insights they didn’t even know to look for—and turn those insights into real business improvements.



### Main Idea
**MapReduce is powerful but limited to batch processing.**
It is <u>not suitable for fast, interactive queries.</u> However, **Hadoop has evolved into a broad ecosystem** that supports <u>many different data processing styles beyond batch jobs</u>.



### Key Points Explained

1. Limitations of MapReduce

   + Designed for offline, **batch processing.**

   + Jobs usually take **minutes or longer**.

   + Not suitable when humans expect **instant or near-instant results**.

2. Hadoop is now an ecosystem, not just MapReduce

   + “Hadoop” often refers to a **collection of tools**, not just HDFS and MapReduce.

   + Many projects are developed under the **Apache Software Foundation.**

3. HBase: online data access

   + A **key-value store** built on top of HDFS.

   + Supports **fast reads and writes** of individual records.

   + Also supports batch operations.

   + Useful for building **data-driven applications**, not just analytics.

4. YARN: the big architectural shift

   + YARN manages **cluster resources.**

   + Allows multiple **processing frameworks** (not only MapReduce) to run on the same cluster.

   + This flexibility enabled the growth of new data processing models.

5. New processing patterns on Hadoop

   + Interactive SQL:
     Tools like Impala or Hive on Tez provide **low-latency SQL** queries on large datasets.

   + Iterative processing:
     Frameworks like **Spark** keep data in memory, ideal for **machine learning** and exploratory analysis.

   + Stream processing:
     Systems like **Storm, Spark Streaming, and Samza** process **real-time data** streams.

   + Search:
     **Solr** can index and search data stored in HDFS.

6. MapReduce still matters

   + It remains useful for **large-scale batch jobs.**

   + Understanding MapReduce helps grasp **core distributed computing concepts** used across the Hadoop ecosystem.
   + 

### Bottom Line

> **Hadoop has grown beyond batch processing into a flexible data platform.**
> While MapReduce remains important for batch workloads, tools like YARN, Spark, HBase, and interactive SQL engines allow Hadoop to support real-time, iterative, and interactive data processing at scale.



### RDBMS vs Hadoop
**Hadoop (MapReduce) and relational databases solve different problems.**
Hadoop is not a replacement for traditional databases; it **complements them**, especially for large-scale, batch data analysis.



### Key Points Explained
1. Why not just use relational databases?

   + Disk **seek time** (finding data) improves slowly compared to transfer speed (streaming data).

   + Databases rely heavily on **random access (seeks)** using indexes (B-Trees).

   + Hadoop is optimized for **streaming large amounts of data sequentially**, which is much faster at scale.

2. When RDBMS works best

   + Small to medium data sizes (gigabytes).

   + **Interactive queries** and frequent updates.

   + Strong guarantees: **ACID transactions**, data integrity, and consistency.

   + Well-structured, schema-defined data.

3. When Hadoop / MapReduce works best

   + Very large datasets (terabytes to petabytes).

   + **Batch analysis over the entire dataset.**

   + Data is **written once and read many times**.

   + Less concern for transactions and strict integrity.

   + Linear scalability across many machines.

4. Key architectural differences (simplified table meaning)

   + **Schema-on-write (RDBMS)**: data must match schema before storage.

   + **Schema-on-read (Hadoop)**: structure is applied when data is read.

   + **Scaling**: RDBMS scaling is complex and non-linear; Hadoop scales linearly by adding machines.

   + **Transactions**: RDBMS supports ACID; MapReduce does not.

5. Structured vs unstructured data

   + RDBMS excels at **structured data** (tables, fixed schemas).

   + Hadoop excels at **semi-structured and unstructured data** (logs, text, images).

   + Hadoop avoids expensive data loading—data is just copied in.

6. Normalization vs locality

   + Databases normalize data to reduce redundancy.

   + Hadoop prefers **denormalized data** to allow fast, local reads.

   + Log files are ideal for Hadoop because they are naturally denormalized.

7. Joins and scalability

   + Hadoop can perform joins, but they are **more expensive** than in databases.

   + Hadoop’s processing models **scale** linearly:

     + Double the data → double the time

     + Double the cluster → same runtime

   + SQL queries generally do not scale this cleanly.



> **Bottom Line**
> **Use RDBMS for fast, transactional, structured data access.**
> Use Hadoop for large-scale, batch analysis of massive, semi-structured or unstructured datasets.
>
> They are increasingly borrowing ideas from each other, but their **core strengths remain** different.
>



### Main Idea
Hadoop/MapReduce and volunteer computing (like SETI@home) both use parallelism, but they are designed for very different environments and problems.



### Key Points Explained

1. What volunteer computing is

   + Projects like **SETI@home, Folding@home, and GIMPS** use idle CPUs from volunteers’ personal computers.

   + Problems are split into small **work units** and sent over the internet.

   + Each unit can take **hours or days** to compute.

   + Results are verified by sending the same work unit to multiple machines.

2. Why SETI@home works

   + The tasks are **CPU-intensive**, but the data size per task is small.

   + Network transfer time is negligible compared to computation time.

   + Volunteers donate **CPU power,** not network bandwidth or storage.

3. How MapReduce is different

   + Designed for **data-intensive workloads**, not just CPU-heavy ones.
   + Runs on **trusted, dedicated machines** in a single data center.

   + Uses **high-bandwidth networks** and **data locality** (move computation to where data is).
   + Jobs typically run for **minutes or hours,** not continuously.

4. Key architectural difference

   + **SETI@home:** computation moves to many remote machines over slow, unreliable networks.

   + **MapReduce:** computation runs close to large datasets stored locally on cluster nodes.



### Bottom Line
> SETI@home scales computation by donating CPU cycles across the internet.
> MapReduce scales data processing by bringing computation to the data in high-bandwidth data centers.

They may look similar at a high level, but they are optimized for **fundamentally different kinds of problems**.



### Hadoop life cycle

**Apache Hadoop was born from the need to process web-scale data cheaply and reliably**, inspired by Google’s internal systems, and evolved into a widely adopted big data platform.



### Key Points Explained
1. Origins of Hadoop

   + Created by **Doug Cutting**, originally as part of **Apache Nutch**, an open-source web search engine.

   + Nutch needed to scale to **billions of web pages,** which traditional systems could not handle.

2. Inspiration from Google

   + Google published papers on:

     + GFS (Google File System) in 2003

     + MapReduce in 2004

   + These papers showed how to store and process massive data on **commodity hardware**.

   + Nutch developers implemented open-source equivalents:

     + NDFS → HDFS

     + MapReduce

3. Birth of Hadoop

   + In **2006**, NDFS and MapReduce were separated from Nutch and became **Hadoop**, a standalone project.

   + Around the same time, **Yahoo! hired Doug Cutting,** providing resources to run Hadoop at web scale.

4. Hadoop at Yahoo!

   + Yahoo! needed to process extremely large web graphs (hundreds of billions of URLs and links).

   + They replaced their internal system with Hadoop because:

     + It already worked in production

     + It scaled well

     + It was open source

   + By **2008**, Yahoo! was running Hadoop on **10,000 cores** for production search.

5. Apache project and industry adoption

   + In **2008**, Hadoop became a **top-level Apache project**, showing strong community support.

   + Major companies adopted Hadoop, including:

     + Yahoo!

     + Facebook

     + Last.fm

     + The New York Times

6. High-profile successes

   + **New York Times** processed 4 TB of scanned archives on Amazon EC2 in under 24 hours.

   + Hadoop repeatedly set **world records for large-scale data sorting.**

   + Later systems like **Spark** continued this trend, sorting even larger datasets faster.

7. Hadoop today

   + Hadoop is now a **mainstream enterprise platform.**

   + It is supported by:

     + Large vendors (IBM, Microsoft, Oracle, EMC)

     + Hadoop-focused companies (Cloudera, Hortonworks, MapR)

   + It is recognized as a g**eneral-purpose storage and data analysis platform** for big data.



### Bottom Line

> Hadoop emerged from open-source search research, was inspired by Google’s breakthroughs, proven at Yahoo!’s web scale, and evolved into a widely adopted enterprise platform for big data storage and analysis.
>
> 

Its success comes from being scalable, fault-tolerant, open source, and affordable, making big data processing accessible beyond just tech giants.



### Main Idea
**The book is a structured guide to Hadoop**, starting from fundamentals, moving through advanced processing and administration, and ending with real-world use cases. It allows **flexible reading paths** depending on your goals.



### Key Points Explained
1. Overall structure

   + The book has **five main parts:**

     + **Parts I–III:** Core Hadoop concepts

     + **Part IV:** Hadoop ecosystem projects

     + **Part V:** Real-world case studies

       

2. Part I – Hadoop fundamentals (must-read)

+ Introduces the core building blocks of Hadoop.

+ Covers:

  + Hadoop overview

  + MapReduce basics

  + HDFS in depth

  + YARN (resource management)

  + Hadoop I/O (data formats, compression, integrity)

  + Essential for understanding later chapters.

3. Part II – **MapReduce in depth**

   + Focuses on **how to write and understand MapReduce programs.**

   + More technical and detailed.

   + Can be **skipped on a first read** if your focus is higher-level tools.

4. Part III – Hadoop administration

   + Covers **setting up, running, and maintaining** a Hadoop cluster.

   + Useful for operators and platform engineers.

5. Part IV – Hadoop ecosystem projects

   + Each chapter is mostly independent.

   + Topics include:

     + **Data formats:** Avro, Parquet

     + **Data ingestion:** Flume, Sqoop

     + **Data processing:** Pig, Hive, Crunch, Spark

     + **Databases and coordination:** HBase, ZooKeeper

   + Emphasizes **higher-level abstractions** over MapReduce.

6. Part V – Case studies
   + Real-world examples showing how Hadoop is used in practice.

7. Appendixes
   + Practical extras like installation and setup instructions.



### Bottom Line

> **The book is both a learning path and a reference.**
> Start with the fundamentals, dive deeper where needed, and explore the ecosystem and real-world applications as your understanding grows.



### Main Idea
MapReduce is a **simple but powerful programming model for processing very large datasets in parallel,** making big data analysis accessible when you have many machines.



### Key Points Explained

1. What MapReduce is

   + A **programming model for data processing.**

   + Simple to understand, yet powerful enough for real-world problems.

   + Programs can be written in **multiple languages** (Java, Python, Ruby).

   + Designed to run **in parallel**, automatically scaling across many machines.

2. Why MapReduce fits big data

   + Works best when you want t**o process all of a large dataset**, not just a small part.

   + Ideal for **semi-structured, record-oriented data.**

3. Example dataset: weather data

   + Weather sensors collect data **hourly from many locations worldwide**.

   + Produces a **large volume of log-style data,** making it a good MapReduce use case.

4. Data format

   + Data comes from the **National Climatic Data Center (NCDC).**

   + Stored as **line-oriented ASCII text.**

   + Each line is a single record with **fixed-width fields** (no delimiters).

   + Fields include date, location, temperature, pressure, etc.

5. Dataset organization

   + Data is stored by **year and weather station**.

   + Originally consisted of **many small files** (one per station per year).

   + For efficient processing, files were **merged into one large file per year**.

   + Fewer large files are easier and faster for Hadoop to process than many small ones.



### Bottom Line

> **MapReduce shines when processing large, semi-structured datasets end-to-end.**
> By automatically parallelizing work across machines, it enables efficient analysis of massive data volumes—like decades of global weather records—with relatively simple programs.



### Main Idea

**Unix tools can analyze large datasets, but they don’t scale well.**
This example shows why frameworks like **Hadoop** are needed for reliable, large-scale parallel data processing.



### Key Points Explained

1. Baseline analysis using Unix tools

   + The question: **What is the highest temperature recorded each year?**

   + A **bash + awk** script processes the weather data.

   + It:

     + Reads each year’s file

     + Extracts temperature and quality fields

     + Filters invalid readings

     + Tracks the maximum temperature per year

2. Correctness and performance

   + Results are correct and easy to understand.

   + Processing one **century of data took ~42 minutes** on a single powerful machine.

   + This provides a **performance baseline** to compare against Hadoop later.

3. Why not just parallelize with Unix tools?
   Although possible in theory, it’s problematic in practice:

   + **Uneven workloads**

     + Yearly files differ greatly in size.

     + Some processes finish early while others take much longer.

     + Overall runtime is limited by the slowest task.

   + Result combination complexity

     + Parallel tasks produce partial results.

     + Additional logic is needed to merge results correctly (e.g., max of maxes).

   + Single-machine limits

     + You’re limited by the CPU, memory, and I/O of one machine.

     + Very large datasets may not even fit on one system.

   + Lack of fault tolerance

     + If a process fails, manual recovery is needed.

     + Coordination across processes becomes complex.

4. Why Hadoop helps

   + Hadoop:

     + Automatically splits data into chunks

     + Runs tasks in parallel across machines

     + Combines results safely

     + Handles failures and retries

   + This removes much of the **messy, error-prone work.**



### Bottom Line



> **Unix tools work well for small to medium datasets, but they don’t scale cleanly.**
> Hadoop provides structured parallelism, fault tolerance, and scalability, making large-scale data analysis far simpler and more reliable.



### Goal

Compute the **maximum recorded temperature per year** using **Hadoop MapReduce**, taking advantage of **parallel processing across a cluster.**



### Core MapReduce Concept

MapReduce splits processing into two phases:

1. Map Phase

  + Input: key–value pairs

  + Output: key–value pairs

  + Programmer defines:

    + map() function

    + Output key/value types

2. Reduce Phase

  + Input: grouped key–value pairs by key

  + Output: final results
  + 

Hadoop handles:

+ Data splitting

+ Parallel execution

+ Sorting & grouping

+ Fault tolerance



------

**Map Phase (Data Preparation)**
Input to the Mapper

+ Key: byte offset of the line in the file (ignored)

+ Value: one line of raw NCDC weather data (text)

Example input:

```bash
(offset, "0067011990999991950051507004...N9+00001...")
```



**What the Map Function Does**
For each line:

1. Extract:

   + Year

   + Air temperature

2. Convert temperature to an integer

3. **Filter out bad records:**

   + Missing temperature (9999)

   + Bad quality codes

4. Emit:

```bash
(year, temperature)
```





**Example Mapper Output**



```bash
(1950, 0)
(1950, 22)
(1950, -11)
(1949, 111)
(1949, 78)
```





The mapper’s job is not aggregation, just cleaning and structuring data.

------



**Shuffle & Sort (Framework’s Job)**

Between map and reduce, Hadoop automatically:

+ Sorts records by key

+ Groups values with the same key

**Reducer Input**



```bash
(1949, [111, 78])
(1950, [0, 22, -11])
```





This step is critical and **completely handled by Hadoop.**



------





**Reduce Phase (Aggregation)**
What the Reduce Function Does
For each year:

+ Iterate through the list of temperatures

+ Find the maximum value

**Reducer Output**

```bash
(1949, 111)
(1950, 22)
```


This is the **final result:**

> Highest global temperature recorded for each year
>



**Why This Works Well in Hadoop**

+ Each mapper works **independently** on different data splits

+ Reducers only see **relevant grouped data**

  + Hadoop manages:

  + Parallelism

  + Load balancing

  + Node failures

  + Data locality



------



**Key Takeaway**

> Map = filter & prepare data
> Reduce = aggregate results



This clean separation is what makes MapReduce scalable, fault-tolerant, and well-suited for large datasets like global weather records.



### Goal

1. MapReduce Job vs Tasks
  **MapReduce Job**
  A **MapReduce job** is the complete unit of work submitted by the client. It consists of:

  + Input data

  + MapReduce program (map + reduce logic)

  + Configuration (number of reducers, input format, etc.)

​	**Tasks**
​	Hadoop breaks a job into **tasks**:

 + **Map tasks**			

+ **Reduce tasks**

Tasks are:

+ Scheduled by **YARN**

+ Executed on cluster nodes

+ Automatically **re-run on failure** (on another node)

------



2. **Input Splits and Map Tasks**
  **Input Splits**

  + Input data is divided into fi**xed-size pieces** called **input splits**

  + One **map task per split**

  + Default split size = **HDFS block size (128 MB)**

**Why Split Size Matters**
**Smaller splits**

+ Better load balancing

+ Faster nodes process more splits

+ More resilience to slow or failed tasks

Too small splits

+ Too many map tasks

+ High task scheduling and startup overhead

➡️ Best practice: split size ≈ HDFS block size

------



3. Data Locality Optimization
Hadoop tries to minimize network usage by running map tasks **where the data lives.**

Levels of Locality

1. Data-local

   + Map task runs on the same node that stores the HDFS block

   + Best performance

2. Rack-local

   + Same rack, different node

   + Requires rack-level network transfer

3. Off-rack

   + Different rack

   + Most expensive (cross-rack bandwidth)

Why Split Size = Block Size?

+ An HDFS block is guaranteed to exist entirely on one node	

+ A split spanning multiple blocks would almost always require network transfer



------



4. Map Output Handling
**Where Map Output Goes**
**Local disk,** not HDFS

Why?

+ Map output is **intermediate**

+ Reduce tasks consume it soon after

+ Replicating it in HDFS would waste disk and bandwidth

Fault Tolerance

+ If a mapper node fails:

  + Hadoop reruns the map task

  + Map output is regenerated automatically

  ------

  

5. Reduce Tasks and Network Transfer
  Reduce Input
  + A reduce task typically needs **output from all map tasks**	
  + Therefore:
    + Reduce tasks **cannot benefit from data locality**

**Data Movement**

+ Mapper outputs are:

  + Sorted

  + Transferred across the network

  + Merged on the reducer node

This phase is called the **shuffle**.

------



6. Reduce Output

  + Reduce output is **final**

  + Stored in **HDFS**

  + HDFS replication applies:

    + First replica local

    + Additional replicas on off-rack nodes

This network usage is **normal HDFS write traffic,** not special MapReduce overhead.

------



7. Number of Reduce Tasks

  + Independent of input size

  + Explicitly configured by the user

  + Affects:

    + Parallelism

    + Output file count

    + Shuffle cost

**Single Reducer**

+ Simple logic

+ All map output goes to one node

+ Can become a bottleneck

**Multiple Reducers**

+ Map output is partitioned

+ One partition per reducer

+ All records for a given key go to exactly one reducer

------



8. Partitioning
  **Default Partitioner**

  + Uses a hash of the key

  + Evenly distributes keys in most cases

**Custom Partitioner**

+ Useful when:

  + Data skew exists

  + Specific key grouping is required

------



9. The Shuffle Phase
When multiple reducers are used:

+ Each reducer:
  + Fetches partitions from all mappers

+ This many-to-many data transfer is called the shuffle

Why it matters:

+ Most complex part of MapReduce

+ Major performance tuning area

+ Network and disk intensive

------



10. Map-Only Jobs (Zero Reducers)
    Some jobs don’t need reducers:

    + Each record processed independently

    + No aggregation required

Characteristics

+ No shuffle phase	

+ Map tasks write output directly to HDFS

+ Minimal network usage

------

**Big Picture Summary**

```bash
Input Data (HDFS)
     ↓
Input Splits
     ↓
Map Tasks (data-local if possible)
     ↓
Local Map Output
     ↓
Shuffle & Sort (network transfer)
     ↓
Reduce Tasks
     ↓
Final Output (HDFS)

```



**Key Takeaways**

+ Splits = parallelism

+ Data locality = performance

+ Shuffle = costliest phase

+ Reducers = aggregation & ordering

+ Fault tolerance is automatic

This architecture is what allows Hadoop MapReduce to **scale reliably across thousands of machines**.



------



### What Is a Combiner Function?

A **combiner** is a **mini-reducer** that runs **after the map phase and before the shuffle**.

Its job:

> Reduce the amount of data sent over the network
>

Instead of sending every `(key, value)` from mappers to reducers, Hadoop may:

+ Run the combiner locally on each mapper’s output

+ Shrink many values into fewer values

+ Then shuffle only the reduced data

📉 Less data → less network traffic → faster jobs

------

**Very Important Rule (The Combiner Contract)**
Hadoop gives **NO guarantees** about the combiner:

+ It may run 0 times

+ Or 1 time

+ Or many times

So your program **must still produce correct output** in all cases.

> **This means:**
> Applying the combiner any number of times must **not change the final result**

Formally:

```bash
reduce(all values)
=
reduce(combine(partitions of values))
```





**Why `max()` Works as a Combiner**
Example: Maximum Temperature
Mapper outputs:



```bash
Map 1:
(1950, 0)
(1950, 20)
(1950, 10)

Map 2:
(1950, 25)
(1950, 15)
```





### Without combiner

Reducer sees:

```bash
(1950, [0, 20, 10, 25, 15])
→ max = 25
```





**With combiner**
Each mapper runs a combiner:

```bash
Map 1 → (1950, 20)
Map 2 → (1950, 25)
```





Reducer sees:

```bash
(1950, [20, 25])
→ max = 25
```



**Why this works**
Because:

```bash
max(0, 20, 10, 25, 15)
=
max(max(0, 20, 10), max(25, 15))
=
max(20, 25)
=
25
```



✅ Correct in all cases

------



**Why `mean()` Does NOT Work as a Combiner**
Let’s try the same idea with averages.

**True mean:**

```bash
mean(0, 20, 10, 25, 15) = 14
```

Mean of means:

```bash
mean(mean(0, 20, 10), mean(25, 15))
= mean(10, 20)
= 15 ❌
```



🚨 Wrong result

**Why?**
Because **mean is not associative**
You lose information (count) when combining partial results.

------



**The Math Rule (Footnote Explained)**
Only functions that are:

+ Associative

+ Commutative

can safely be used as combiners.

**Safe examples**
	

| Operation | Combiner-safe?                  |
| --------- | ------------------------------- |
| max       | ✅                               |
| min       | ✅                               |
| sum       | ✅                               |
| count     | ✅                               |
| mean      | ❌ (unless you emit sum + count) |



------



**Important: Combiner ≠ Reducer Replacement**
A combiner:

+ **Does not replace** the reducer

+ Only runs **within a single mapper’s output**

+ Reducer still needed to combine data from **different mappers**

Think of it like this:


```bash
Mapper → Combiner → Shuffle → Reducer
```





**Why You Should Almost Always Consider a Combiner**
Even though it’s optional:

+ It can **dramatically reduce shuffle size**

+ It often costs almost nothing to implement

+ Hadoop decides whether and how often to run it

➡️ If your reduce logic is combiner-safe, use it

------



**How the Combiner Is Specified in Java**
In your example, the combiner logic is identical to the reducer logic.

```java
job.setCombinerClass(MaxTemperatureReducer.class);
job.setReducerClass(MaxTemperatureReducer.class);
```



This is common and totally valid when:

+ The reduce function is associative and commutative

+ Output key/value types match

**Full Flow in This Job**

```bash
Map:        (year, temperature)
Combiner:   (year, local max)
Reducer:    (year, global max)
```



------

**Key Takeaways (Burn These In 🔥)**

+ Combiner = optimization

+ Hadoop may skip it entirely

+ Must be safe to run multiple times

+ Works best for:

  + max / min

  + sum

  + count

+ Mean requires extra bookkeeping

+ Same class as reducer is often reused



------



The key distinction is who controls the flow of records.

### Java MapReduce API: framework-driven (“push” model)

In the Java MapReduce API, Hadoop is in control:

+ Hadoop reads the input data

+ It splits the data into records (usually one line = one record)

+ For each record, Hadoop **calls your `map()`** method

+ Your mapper reacts to each call

So the execution model looks like this conceptually:

```bash
for each record:
    mapper.map(key, value)
```





Because of this:

+ Your mapper naturally thinks in terms of **one record at a time**

+ If you want to process multiple records together (for example, grouping lines):

  + You must **store state** in instance variables

  + Accumulate records as they arrive

  + Use the `cleanup()` method to flush any remaining data at the end

This pattern works, but it’s slightly awkward because:

+ You are adapting a streaming problem to a record-at-a-time API

+ You must be careful with memory usage and lifecycle semantics



------

**Hadoop Streaming: program-driven (“pull” model)**

With Hadoop Streaming, the control is flipped:

+ Hadoop sends the mapper input to **stdin**

+ Your program decides:

  + how to read input

  + how many lines to read at once

  + when to emit output

So the model becomes:

```bash
while read from stdin:
    process however you want
    emit key/value pairs
```





This gives you **more flexibility:**

+ You can:

  + Read line by line

  + Read blocks of lines

  + Buffer input

  + Implement custom grouping logic naturally

+ No need for `cleanup()` tricks

+ The program ends → processing ends (simple and intuitive)

This is why Streaming often feels more Unix-like and natural for text processing.

------



**Practical implications**
Java API advantages

+ Better performance (no external process overhead)

+ Strong typing and compile-time checks
+ Better integration with Hadoop internals

+ Preferred for large, production-grade pipelines

Streaming advantages

+ Faster to prototype

+ Language-agnostic (Python, Ruby, Bash, Perl, etc.)

+ Natural for:

  + Text-heavy workflows

  + Log processing

  + Existing Unix tools

+ Easier mental model for many engineers

------

**Summary (the mental model to keep)**

+ Java MapReduce

  + Hadoop controls iteration

  + Mapper is called per record

  + “Pushed” records

+ Hadoop Streaming

  + Your program controls iteration

  + You pull data from stdin

  + Full control over how input is consumed

This distinction becomes especially important when:

+ Processing multi-line records

+ Handling complex grouping logic

+ Migrating Unix pipelines to Hadoop



------



**Why HDFS Looks the Way It Does**
All of HDFS’s design choices follow directly from the **assumptions** laid out above. Once you accept that:

+ files are **huge**

+ access is **streaming**

+ hardware **fails regularly**

then HDFS’s behavior starts to feel not only reasonable, but inevitable.

Let’s unpack the implications.



**Very Large Files → Block-Based Storage**
HDFS stores files by splitting them into **large fixed-size blocks** (128 MB by default).

This has several advantages:

+ Reduces metadata overhead (fewer blocks than traditional filesystems)

+ Enables parallel processing:
  + different blocks of the same file can be processed simultaneously

+ Makes disk throughput the dominant factor, not seek time

Unlike traditional filesystems:

+ Blocks are not tightly coupled to a specific disk

+ Blocks are independently replicated across the cluster

This block abstraction is the foundation that allows MapReduce (and later Spark) to scale.



**Streaming Access → High Throughput, Not Low Latency**
HDFS is optimized for **bandwidth**, not responsiveness.

That’s why:

+ Reading a file sequentially is very fast

+ Random reads are slow

+ Opening a file has higher overhead than local filesystems

This trade-off makes sense when:

+ You are scanning terabytes of data

+ The job runs for minutes or hours

+ Startup latency is irrelevant compared to total runtime

This is also why HDFS pairs so well with:

+ MapReduce

+ Spark

+ Hive

+ Batch analytics in general

And why it’s a poor choice for:

+ Web serving

+ User-facing APIs

+ Transactional workloads
+ 

**Commodity Hardware → Replication, Not RAID**
Instead of relying on expensive hardware or RAID controllers, HDFS assumes:

> **Machines will fail. Disks will fail. Networks will fail.**

So it handles failure in software.

**Replication**
Each HDFS block is replicated (default: 3 copies):

+ One replica on the local node

+ One on a different node in the same rack

+ One on a node in a different rack

This gives:

+ Fault tolerance (disk or node failure)

+ Rack awareness (rack switch failure)

+ High read availability

If a node dies:

+ The namenode notices missing replicas

+ New replicas are created automatically

+ No user intervention required

Failure is not exceptional in HDFS—it’s expected.



**Why HDFS Is Bad at Small Files**
This is one of the most common real-world pain points.

The namenode keeps **all filesystem metadata in RAM**, including:

+ filenames

+ directory structure

+ permissions

+ block locations

This gives fast metadata access—but at a cost.

Since each file consumes memory:

+ Millions of files → manageable

+ Billions of files → impossible

This is why common mitigation strategies exist:

+ HAR files

+ HBase

+ Ozone

+ Packing small files into larger containers

+ Using object stores (S3, GCS) instead of HDFS

HDFS was never meant to be a POSIX filesystem replacement.



**Single Writer, Append-Only → Simplicity and Safety**
HDFS enforces a **simple consistency model:**

+ One writer per file

+ Writes only at the end

+ No random updates

Why?

Because supporting:

+ multiple writers

+ random writes

+ file locking

would dramatically complicate:

+ consistency guarantees

+ recovery logic

+ performance

Instead, HDFS follows a **batch-processing worldview:**

+ Generate data

+ Write once

+ Analyze many times

+ Delete or archive

This matches the MapReduce model perfectly.



**The Big Picture**
HDFS is not a general-purpose filesystem.

It is a **specialized storage layer** designed for:

+ Massive datasets

+ Sequential access

+ Parallel computation

+ Fault tolerance at scale

If you judge it by desktop or database filesystem standards, it looks restrictive.
If you judge it by **big data requirements**, it’s elegant.



------





**1️⃣ What a “block” means in normal filesystems**
On a s**ingle machine:**

+ **Disk block**: usually **512 bytes**

+ **Filesystem block:** usually **4 KB – 64 KB**

You don’t see these directly:

+ You read/write files

+ The filesystem quietly maps them to blocks

Tools like `df` or `fsck` care about blocks, not you.



**2️⃣ What a block means in HDFS**
HDFS also uses blocks—but **much bigger** ones:

+ **Default HDFS block size: 128 MB**

+ Some clusters use **256 MB / 512 MB / 1 GB**

Key differences vs local filesystems:

✅ Files are split into **block-sized chunks**
✅ Each block is stored **independently**
✅ Blocks can live on **different machines**
✅ A small file **does NOT waste space**

Example:

```bash
Block size = 128 MB
File size  = 1 MB
Disk used  = 1 MB  (not 128 MB)
```



That’s an important point—HDFS blocks are logical units, not preallocated space.





**3️⃣ Why HDFS blocks are so large**

This is the **core design reason** 👇

Disk reality:

+ **Seek time** ≈ 10 ms

+ **Transfer speed** ≈ 100 MB/s

If you read:

+ 4 KB → you pay seek cost almost entirely

+ 128 MB → seek cost is almost irrelevant

Rough math from the book:

+ 10 ms seek

+ Want seek = only 1% of total time

+ Need ~100 MB of data transfer

➡️ Hence **128 MB blocks**

HDFS is optimized for:

> **“Read a lot of data sequentially”**

Not:

> “Jump around randomly”





**4️⃣ Why this fits MapReduce perfectly**
MapReduce design assumption:

+ One map task ≈ one HDFS block

So:

+ 1 TB file

+ 128 MB blocks

+ ~8,000 blocks

+ ~8,000 map tasks

This gives:

+ Massive parallelism

+ Good load balancing

+ Sequential disk reads

+ High throughput

⚠️ But there’s a tradeoff:

+ If blocks are too large → too few map tasks → poor parallelism

+ If blocks are too small → too many tasks → overhead dominates

That’s why block size matters.



**5️⃣ Why blocks make HDFS scalable and simple**
✅ Files can be bigger than any disk
A file can:

+ Span dozens, hundreds, or thousands of disks

+ Even fill the entire cluster in theory

No single machine limitation.



✅ Storage management is simpler
HDFS stores:

+ **Blocks** on DataNodes

+ **Metadata** on the NameNode

Blocks:

+ Fixed size

+ Easy to count

+ Easy to place

+ Easy to replicate

Metadata (filename, permissions, block mapping):

+ Stored separately

+ Doesn’t pollute storage logic

This separation is **huge** for reliability.



**6️⃣ Blocks + replication = fault tolerance**
Each block is usually:

+ **Replicated 3 times**

+ Stored on **different machines**

+ Often across **different racks**

If:

+ Disk dies → read another replica

+ Node dies → read another replica

+ Block corrupt → re-replicated automatically

To the client:

> “Nothing happened.”
>

That’s the magic.

You can even:

+ Increase replication for “hot” files

+ Spread read load across the cluster



**7️⃣ Why fsck talks about blocks**
HDFS tools think in blocks, not files.

Example:

```bash
hdfs fsck / -files -blocks
```





You’ll see:

+ Each file

+ Each block ID

+ Which DataNodes store each replica

Because **blocks are the real physical units** of HDFS.



**Mental model (very important)**
**Local filesystem**

> File → blocks → disk



**HDFS**

> File → blocks → machines → disks

Blocks are the currency HDFS trades in.



**One-sentence takeaway**

> HDFS uses very large blocks to minimize disk seeks, maximize streaming throughput, simplify storage, and enable massive parallel processing with fault tolerance.















