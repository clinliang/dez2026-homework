cll@PC-LIANG:/mnt/d/github/dez2026-homework/m2_proj_workflow_kestra_nyc_taxi$ docker-compose up --force-recreate
[+] up 10/10
 ✔ Image kestra/kestra:v1.1        Pulled                                                                                                                           1.5s 
 ✔ Network m2_kestra_default       Created                                                                                                                          0.0s 
 ✔ Volume m2_kestra_pgadmin_data   Created                                                                                                                          0.0s 
 ✔ Volume m2_kestra_pgdata         Created                                                                                                                          0.0s 
 ✔ Volume m2_kestra_kestra_pgdata  Created                                                                                                                          0.0s 
 ✔ Volume m2_kestra_kestra_data    Created                                                                                                                          0.0s 
 ✔ Container m2_kestra-db-1        Created                                                                                                                          0.1s 
 ✔ Container m2_kestra-kestra_db-1 Created                                                                                                                          0.1s 
 ✔ Container m2_kestra-kestra-1    Created                                                                                                                          0.1s 
 ✔ Container m2_kestra-pgadmin-1   Created                                                                                                                          0.1s 
Attaching to db-1, kestra-1, kestra_db-1, pgadmin-1
Container m2_kestra-kestra_db-1 Waiting 
kestra_db-1  | The files belonging to this database system will be owned by user "postgres".
kestra_db-1  | This user must also own the server process.
kestra_db-1  | 
kestra_db-1  | The database cluster will be initialized with locale "en_US.utf8".
kestra_db-1  | The default database encoding has accordingly been set to "UTF8".
kestra_db-1  | The default text search configuration will be set to "english".
kestra_db-1  | 
kestra_db-1  | Data page checksums are enabled.
kestra_db-1  | 
kestra_db-1  | fixing permissions on existing directory /var/lib/postgresql/18/docker ... ok
kestra_db-1  | creating subdirectories ... ok
kestra_db-1  | selecting dynamic shared memory implementation ... posix
kestra_db-1  | selecting default "max_connections" ... 100
db-1         | The files belonging to this database system will be owned by user "postgres".
db-1         | This user must also own the server process.
db-1         | 
db-1         | The database cluster will be initialized with locale "en_US.utf8".
db-1         | The default database encoding has accordingly been set to "UTF8".
db-1         | The default text search configuration will be set to "english".
db-1         | 
db-1         | Data page checksums are enabled.
db-1         | 
db-1         | fixing permissions on existing directory /var/lib/postgresql/18/docker ... ok
db-1         | creating subdirectories ... ok
db-1         | selecting dynamic shared memory implementation ... posix
kestra_db-1  | selecting default "shared_buffers" ... 128MB
db-1         | selecting default "max_connections" ... 100
kestra_db-1  | selecting default time zone ... Etc/UTC
kestra_db-1  | creating configuration files ... ok
db-1         | selecting default "shared_buffers" ... 128MB
db-1         | selecting default time zone ... Etc/UTC
db-1         | creating configuration files ... ok
kestra_db-1  | running bootstrap script ... ok
pgadmin-1    | email config is {'CHECK_EMAIL_DELIVERABILITY': False, 'ALLOW_SPECIAL_EMAIL_DOMAINS': [], 'GLOBALLY_DELIVERABLE': True}
db-1         | running bootstrap script ... ok
kestra_db-1  | performing post-bootstrap initialization ... ok
db-1         | performing post-bootstrap initialization ... ok
kestra_db-1  | syncing data to disk ... ok
kestra_db-1  | 
kestra_db-1  | 
kestra_db-1  | Success. You can now start the database server using:
kestra_db-1  | 
kestra_db-1  |     pg_ctl -D /var/lib/postgresql/18/docker -l logfile start
kestra_db-1  | 
kestra_db-1  | initdb: warning: enabling "trust" authentication for local connections
kestra_db-1  | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
db-1         | initdb: warning: enabling "trust" authentication for local connections
db-1         | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
db-1         | syncing data to disk ... ok
db-1         | 
db-1         | 
db-1         | Success. You can now start the database server using:
db-1         | 
db-1         |     pg_ctl -D /var/lib/postgresql/18/docker -l logfile start
db-1         | 
kestra_db-1  | waiting for server to start....2026-01-24 07:03:35.623 UTC [51] LOG:  starting PostgreSQL 18.1 (Debian 18.1-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
kestra_db-1  | 2026-01-24 07:03:35.625 UTC [51] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db-1         | waiting for server to start....2026-01-24 07:03:35.635 UTC [53] LOG:  starting PostgreSQL 18.1 (Debian 18.1-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
kestra_db-1  | 2026-01-24 07:03:35.635 UTC [57] LOG:  database system was shut down at 2026-01-24 07:03:34 UTC
db-1         | 2026-01-24 07:03:35.638 UTC [53] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
kestra_db-1  | 2026-01-24 07:03:35.642 UTC [51] LOG:  database system is ready to accept connections
db-1         | 2026-01-24 07:03:35.653 UTC [59] LOG:  database system was shut down at 2026-01-24 07:03:34 UTC
db-1         | 2026-01-24 07:03:35.659 UTC [53] LOG:  database system is ready to accept connections
kestra_db-1  |  done
kestra_db-1  | server started
db-1         |  done
db-1         | server started
kestra_db-1  | CREATE DATABASE
kestra_db-1  | 
kestra_db-1  | 
kestra_db-1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
kestra_db-1  | 
kestra_db-1  | waiting for server to shut down....2026-01-24 07:03:35.868 UTC [51] LOG:  received fast shutdown request
db-1         | CREATE DATABASE
db-1         | 
db-1         | 
db-1         | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
db-1         | 
db-1         | waiting for server to shut down...2026-01-24 07:03:35.872 UTC [53] LOG:  received fast shutdown request
db-1         | .2026-01-24 07:03:35.878 UTC [53] LOG:  aborting any active transactions
kestra_db-1  | 2026-01-24 07:03:35.875 UTC [51] LOG:  aborting any active transactions
kestra_db-1  | 2026-01-24 07:03:35.878 UTC [51] LOG:  background worker "logical replication launcher" (PID 60) exited with exit code 1


kestra_db-1  | 2026-01-24 07:03:35.878 UTC [55] LOG:  shutting down
db-1         | 2026-01-24 07:03:35.880 UTC [53] LOG:  background worker "logical replication launcher" (PID 62) exited with exit code 1




db-1         | 2026-01-24 07:03:35.880 UTC [57] LOG:  shutting down
kestra_db-1  | 2026-01-24 07:03:35.883 UTC [55] LOG:  checkpoint starting: shutdown immediate
db-1         | 2026-01-24 07:03:35.885 UTC [57] LOG:  checkpoint starting: shutdown immediate
kestra_db-1  | 2026-01-24 07:03:36.258 UTC [55] LOG:  checkpoint complete: wrote 943 buffers (5.8%), wrote 3 SLRU buffers; 0 WAL file(s) added, 0 removed, 0 recycled; write=0.030 s, sync=0.327 s, total=0.381 s; sync files=303, longest=0.004 s, average=0.002 s; distance=4352 kB, estimate=4352 kB; lsn=0/1B9FBA0, redo lsn=0/1B9FBA0
db-1         | 2026-01-24 07:03:36.260 UTC [57] LOG:  checkpoint complete: wrote 943 buffers (5.8%), wrote 3 SLRU buffers; 0 WAL file(s) added, 0 removed, 0 recycled; write=0.032 s, sync=0.328 s, total=0.380 s; sync files=303, longest=0.005 s, average=0.002 s; distance=4352 kB, estimate=4352 kB; lsn=0/1B9FBA0, redo lsn=0/1B9FBA0
db-1         | 2026-01-24 07:03:36.282 UTC [53] LOG:  database system is shut down
kestra_db-1  | 2026-01-24 07:03:36.284 UTC [51] LOG:  database system is shut down
kestra_db-1  |  done
kestra_db-1  | server stopped
kestra_db-1  | 
kestra_db-1  | PostgreSQL init process complete; ready for start up.
kestra_db-1  | 
db-1         |  done
db-1         | server stopped
db-1         | 
db-1         | PostgreSQL init process complete; ready for start up.
db-1         | 
kestra_db-1  | 2026-01-24 07:03:36.399 UTC [1] LOG:  starting PostgreSQL 18.1 (Debian 18.1-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
kestra_db-1  | 2026-01-24 07:03:36.399 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
kestra_db-1  | 2026-01-24 07:03:36.399 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db-1         | 2026-01-24 07:03:36.403 UTC [1] LOG:  starting PostgreSQL 18.1 (Debian 18.1-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
db-1         | 2026-01-24 07:03:36.404 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db-1         | 2026-01-24 07:03:36.404 UTC [1] LOG:  listening on IPv6 address "::", port 5432
kestra_db-1  | 2026-01-24 07:03:36.403 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db-1         | 2026-01-24 07:03:36.408 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
kestra_db-1  | 2026-01-24 07:03:36.414 UTC [73] LOG:  database system was shut down at 2026-01-24 07:03:36 UTC
db-1         | 2026-01-24 07:03:36.419 UTC [75] LOG:  database system was shut down at 2026-01-24 07:03:36 UTC
kestra_db-1  | 2026-01-24 07:03:36.420 UTC [1] LOG:  database system is ready to accept connections
db-1         | 2026-01-24 07:03:36.430 UTC [1] LOG:  database system is ready to accept connections
pgadmin-1    | /venv/lib/python3.14/site-packages/sshtunnel.py:1040: SyntaxWarning: 'return' in a 'finally' block
pgadmin-1    |   return (ssh_host,
pgadmin-1    | NOTE: Configuring authentication for SERVER mode.
pgadmin-1    | 
pgadmin-1    | pgAdmin 4 - Application Initialisation
pgadmin-1    | ======================================
pgadmin-1    | 
pgadmin-1    | postfix/postlog: starting the Postfix mail system
pgadmin-1    | [2026-01-24 07:03:58 +0000] [1] [INFO] Starting gunicorn 23.0.0
pgadmin-1    | [2026-01-24 07:03:58 +0000] [1] [INFO] Listening at: http://[::]:80 (1)
pgadmin-1    | [2026-01-24 07:03:58 +0000] [1] [INFO] Using worker: gthread
pgadmin-1    | [2026-01-24 07:03:58 +0000] [123] [INFO] Booting worker with pid: 123
pgadmin-1    | /venv/lib/python3.14/site-packages/sshtunnel.py:1040: SyntaxWarning: 'return' in a 'finally' block
pgadmin-1    |   return (ssh_host,
Container m2_kestra-kestra_db-1 Healthy 
kestra-1     | 07:04:08.490 WARN  main         i.m.p.PrometheusMeterRegistry The meter (MeterId{name='netty.alloc.arena.allocation.count', tags=[tag(arena.number=0),tag(memory=direct),tag(size=small)]}) registration has failed: Prometheus requires that all meters with the same name have the same set of tag keys. There is already an existing meter named 'netty_alloc_arena_allocation_count' containing tag keys [arena_number, memory]. The meter you are attempting to register has keys [arena_number, memory, size]. Note that subsequent logs will be logged at debug level.
kestra-1     | 07:04:08.407 INFO  main         org.flywaydb.core.FlywayExecutor Database: jdbc:postgresql://kestra_db:5432/kestra (PostgreSQL 18.1)
kestra-1     | 07:04:08.684 WARN  main         o.f.c.i.database.base.Database Flyway upgrade recommended: PostgreSQL 18.1 is newer than this version of Flyway and support has not been tested. The latest supported version of PostgreSQL is 17.
kestra-1     | 07:04:08.605 INFO  main         o.f.c.i.s.JdbcTableSchemaHistory Schema history table "public"."flyway_schema_history" does not exist yet
kestra-1     | 07:04:08.868 INFO  main         o.f.core.internal.command.DbValidate Successfully validated 43 migrations (execution time 00:00.038s)
kestra-1     | 07:04:08.733 INFO  main         o.f.c.i.s.JdbcTableSchemaHistory Creating Schema History table "public"."flyway_schema_history" ...
kestra-1     | 07:04:08.048 INFO  main         o.f.core.internal.command.DbMigrate Current version of schema "public": << Empty Schema >>
kestra-1     | 07:04:08.065 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.1 - initial"
kestra-1     | 07:04:08.180 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.2 - worker heartbeat"
kestra-1     | 07:04:08.604 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.3 - worker heartbeat"
kestra-1     | 07:04:09.085 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.4 - postgres-queues-pkey"
kestra-1     | 07:04:09.901 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.5 - multitenant"
kestra-1     | 07:04:09.264 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.6 - multitenant on multipleconditions"
kestra-1     | 07:04:09.046 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.7 - execution queued"
kestra-1     | 07:04:09.464 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.8 - execution cancelled"
kestra-1     | 07:04:09.617 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.9 - execution queued"
kestra-1     | 07:04:09.161 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.10 - multitenant indices"
kestra-1     | 07:04:09.664 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.12 - execution triggerid"
kestra-1     | 07:04:09.853 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.13 - log fulltext"
kestra-1     | 07:04:09.107 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.14 - subflow executions"
kestra-1     | 07:04:09.510 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.15 - trigger store next date"
kestra-1     | 07:04:09.148 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.16 - log timestamp index"
kestra-1     | 07:04:09.303 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.17 - service instance"
kestra-1     | 07:04:09.033 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.18 - retry revamp"
kestra-1     | 07:04:09.200 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.19 - retry flow"
kestra-1     | 07:04:09.572 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.20 - drop worker instance"
kestra-1     | 07:04:09.472 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.21 - trigger worker id"
kestra-1     | 07:04:09.304 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.22 - flow with source"
kestra-1     | 07:04:09.754 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.23 - execution queued index"
kestra-1     | 07:04:09.013 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.24 - sla monitor"
kestra-1     | 07:04:09.430 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.25 - dashboard"
kestra-1     | 07:04:09.180 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.26 - skipped"
kestra-1     | 07:04:09.317 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.27 - escape fulltext"
kestra-1     | 07:04:09.206 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.28 - cluster event"
kestra-1     | 07:04:09.990 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.29 - subflow execution end"
kestra-1     | 07:04:09.684 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.30 - delete subflow executions"
kestra-1     | 07:04:09.402 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.31 - queues updated date"
kestra-1     | 07:04:09.953 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.32 - queues index on key"
kestra-1     | 07:04:09.360 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.34 - service instance indices"
kestra-1     | 07:04:09.341 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.35 - triggers index on next execution date"
kestra-1     | 07:04:09.552 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.36 - service instance index on service id"
kestra-1     | 07:04:09.195 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.37 - execution kind"
kestra-1     | 07:04:09.516 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.38 - flow interface"
kestra-1     | 07:04:09.292 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.39 - execution breakpoint"
kestra-1     | 07:04:09.205 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.41 - offset bigint"
kestra-1     | 07:04:09.601 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.43 - multiple condition event"
kestra-1     | 07:04:09.975 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.44 - concurrency-limit"
kestra-1     | 07:04:09.327 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.45 - taskrun submitted"
kestra-1     | 07:04:09.008 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.46 - kv metadata"
kestra-1     | 07:04:09.229 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.47 - taskrun resubmitted"
kestra-1     | 07:04:09.229 INFO  main         o.f.core.internal.command.DbMigrate Successfully applied 43 migrations to schema "public", now at version v1.47 (execution time 00:00.193s)
kestra-1     | 07:04:10.058 INFO  main         i.kestra.core.plugins.PluginScanner Registered 102 core plugins (scan done in 130ms)
kestra-1     | 07:04:10.593 INFO  main         i.k.c.c.s.AbstractServerCommand Machine information: 16 available cpu(s), 3780MB max memory, Java version 21.0.9+10-LTS
kestra-1     | 07:04:10.093 INFO  standalone   io.kestra.cli.AbstractCommand Starting Kestra 1.1.14 with environments [cli] [revision 94be24d / 2026-01-13T14:55]
kestra-1     | 07:04:11.237 INFO  standalone   i.kestra.core.plugins.PluginScanner Registered 922 plugins from 165 groups (scan done in 472ms)
kestra-1     | 07:04:12.066 INFO  standalone   io.kestra.cli.AbstractCommand Server Running: http://ed13aee505d2:8080, Management server on port http://ed13aee505d2:8081/health
kestra-1     | 07:04:13.073 INFO  standalone   i.k.w.services.FlowAutoLoaderService Loaded 6 "Getting Started" flows from community blueprints. You can disable this feature by setting 'kestra.tutorialFlows.enabled=false'.
kestra-1     | 07:04:13.965 INFO  standalone-runner_1 io.kestra.worker.DefaultWorker Worker started with 128 thread(s)
kestra-1     | 07:04:13.602 INFO  standalone-runner_0 io.kestra.jdbc.runner.JdbcExecutor Executor started with 16 thread(s)
kestra-1     | 07:04:13.048 INFO  standalone-runner_3 io.kestra.jdbc.runner.JdbcIndexer Indexer started
kestra-1     | 07:04:13.196 INFO  standalone-runner_2 i.kestra.scheduler.AbstractScheduler Scheduler started
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:24 +0000] "GET / HTTP/1.1" 302 213 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:24 +0000] "GET /login?next=/ HTTP/1.1" 200 2494 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:25 +0000] "GET /browser/js/endpoints.js?ver=91100 HTTP/1.1" 200 16662 "http://localhost:8085/login?next=/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:25 +0000] "GET /tools/translations.js?ver=91100 HTTP/1.1" 200 321 "http://localhost:8085/login?next=/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "POST /authenticate/login HTTP/1.1" 302 205 "http://localhost:8085/login?next=/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /browser/ HTTP/1.1" 200 2933 "http://localhost:8085/login?next=/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /browser/browser.css?ver=91100 HTTP/1.1" 200 4180 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /browser/js/endpoints.js?ver=91100 HTTP/1.1" 200 3738 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /browser/js/messages.js?ver=91100 HTTP/1.1" 200 883 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /browser/js/utils.js?ver=91100 HTTP/1.1" 200 2025 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /tools/translations.js?ver=91100 HTTP/1.1" 200 321 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /browser/server/supported_servers.js?ver=91100 HTTP/1.1" 200 291 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:29 +0000] "GET /user_management/current_user.js?ver=91100 HTTP/1.1" 200 471 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /browser/check_corrupted_db_file HTTP/1.1" 200 61 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /misc/bgprocess/ HTTP/1.1" 200 2 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /preferences/get_all HTTP/1.1" 200 11809 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /settings/get_tree_state/ HTTP/1.1" 200 0 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /browser/nodes/ HTTP/1.1" 200 273 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /sqleditor/new_connection_dialog HTTP/1.1" 200 130 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "POST /browser/master_password HTTP/1.1" 200 166 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /sqleditor/new_connection_dialog HTTP/1.1" 200 130 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /sqleditor/new_connection_dialog HTTP/1.1" 200 130 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /sqleditor/new_connection_dialog HTTP/1.1" 200 130 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:30 +0000] "GET /settings/object_explorer_filter HTTP/1.1" 200 95 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:04:31 +0000] "GET /misc/upgrade_check?trigger_update_check=false HTTP/1.1" 200 77 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
kestra-1     | 07:04:40.697 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:40.455Z | GET / HTTP/1.1 | status: 307 | ip: 172.18.0.1 | length: - | duration: 38
kestra-1     | 07:04:40.127 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:40.499Z | GET /ui/ HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 1225 | duration: 76
kestra-1     | 07:04:41.422 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:40.909Z | GET /api/v1/configs HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 496 | duration: 360
kestra-1     | 07:04:41.474 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:41.275Z | GET /api/v1/basicAuthValidationErrors HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 114 | duration: 7
kestra-1     | 07:04:41.031 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:41.294Z | GET /api/v1/configs HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 496 | duration: 3
kestra-1     | 07:04:41.929 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:41.302Z | GET /api/v1/basicAuthValidationErrors HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 114 | duration: 3
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:05:00 +0000] "POST /settings/save_tree_state/ HTTP/1.1" 200 63 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
pgadmin-1    | ::ffff:172.18.0.1 - - [24/Jan/2026:07:05:00 +0000] "GET /settings/get_tree_state/ HTTP/1.1" 200 2 "http://localhost:8085/browser/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"