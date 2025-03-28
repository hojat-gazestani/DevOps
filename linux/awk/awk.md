# awk apache log

```sh
# awk print apache log time, date and time zone
awk '{print $4,$5}' apache_logs.txt

# awk print entires from just one day of apache log
awk '( $4 ~ /20\/May\/2015/ )' apache_logs.txt

# awk print just the client IP address of apache log
awk '( $4 ~ /20\/May\/2015/ ) { print $1 }' apache_logs.txt

# awk print total number of access to apache  on a given data
awk '( $4 ~ /20\/May\/2015/ ) { print $1 }' apache_logs.txt | wc -l

# awk increment our own variable in the main block
awk '( $4 ~ /20\/May\/2015/ ) { print $1; COUNT++ } END { print COUNT }' apache_logs.txt

# awk count total number without printing 
awk '( $4 ~ /20\/May\/2015/ ) { COUNT++ } END { print COUNT }' apache_logs.txt
```

## awk summarizing 404 error apache log

```sh
# awk apache log status code
awk '{ print $9 }' apache_logs.txt

# awk print the 404 errors
awk '( $9 ~ /404/ ) { print $9 }' apache_logs.txt

# awk apache log print status code and the page that was being accessed 
awk '( $9 ~ /404/ ) { print $9 $7 }' apache_logs.txt

# awk apache log summarize duplicated with sort and uniq
awk '( $9 ~ /404/ ) { print $9 $7 }' apache_logs.txt | sort -u
```

## Summarizing HTTP access codes
``sh

cat status.awk
{ record[$9]++ }
END {
for (r in record)
print r, " has occurred ", record[r], " times."}

awk -f status.awk apache_logs.txt
304  has occurred  445  times.
403  has occurred  2  times.
404  has occurred  213  times.
500  has occurred  3  times.
200  has occurred  9126  times.
206  has occurred  45  times.
416  has occurred  2  times.
301  has occurred  164  times.
```

- summarize the 404 status code
```sh
cat 404.awk
{ if ( $9 == "404" )
	record[$9,$7]++ }
END {
for (r in record)
print r, " has occurred ", record[r], " times."}

awk -f 404.awk apache_logs.txt
```

## awk apache log resources hits

```sh
# awk apache log how many times a specific page or a resource was requested
awk '{ print $7}' apache_logs.txt | sort | uniq -c | sort -rn 

# awk apache log look at the requested PHP files
awk ' ($7 ~ /php/) { print $7}' apache_logs.txt | sort | uniq -c | sort -rn

# awk apache log identify image hotlinking
awk -F'"' '($2 ~ /\.(png|jpg|gif)/ && $4 !~ /^https:\/\/www\.semicomplete\.com/) {print $4}' apache_logs.txt| sort | uniq -c | sort

# 
```
