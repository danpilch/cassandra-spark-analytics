CREATE KEYSPACE spark_demo WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': '1'
};

USE spark_demo;

CREATE TABLE person_data (
  id int,
  email text,
  first_name text,
  gender text,
  ip_address text,
  last_name text,
  PRIMARY KEY (id)
) WITH
  bloom_filter_fp_chance=0.010000 AND
  caching='{"keys":"ALL", "rows_per_partition":"NONE"}' AND
  comment='' AND
  dclocal_read_repair_chance=0.100000 AND
  gc_grace_seconds=864000 AND
  read_repair_chance=0.000000 AND
  default_time_to_live=0 AND
  speculative_retry='99.0PERCENTILE' AND
  memtable_flush_period_in_ms=0 AND
  compaction={'class': 'SizeTieredCompactionStrategy'} AND
  compression={'sstable_compression': 'LZ4Compressor'};
