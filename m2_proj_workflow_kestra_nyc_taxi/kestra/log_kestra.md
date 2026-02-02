cll@PC-LIANG:/mnt/d/github/dez2026-homework/m2_proj_workflow_kestra_nyc_taxi$ docker logs -f m2_kestra-kestra-1
07:04:08.490 WARN  main         i.m.p.PrometheusMeterRegistry The meter (MeterId{name='netty.alloc.arena.allocation.count', tags=[tag(arena.number=0),tag(memory=direct),tag(size=small)]}) registration has failed: Prometheus requires that all meters with the same name have the same set of tag keys. There is already an existing meter named 'netty_alloc_arena_allocation_count' containing tag keys [arena_number, memory]. The meter you are attempting to register has keys [arena_number, memory, size]. Note that subsequent logs will be logged at debug level.
07:04:08.407 INFO  main         org.flywaydb.core.FlywayExecutor Database: jdbc:postgresql://kestra_db:5432/kestra (PostgreSQL 18.1)
07:04:08.684 WARN  main         o.f.c.i.database.base.Database Flyway upgrade recommended: PostgreSQL 18.1 is newer than this version of Flyway and support has not been tested. The latest supported version of PostgreSQL is 17.
07:04:08.605 INFO  main         o.f.c.i.s.JdbcTableSchemaHistory Schema history table "public"."flyway_schema_history" does not exist yet
07:04:08.868 INFO  main         o.f.core.internal.command.DbValidate Successfully validated 43 migrations (execution time 00:00.038s)
07:04:08.733 INFO  main         o.f.c.i.s.JdbcTableSchemaHistory Creating Schema History table "public"."flyway_schema_history" ...
07:04:08.048 INFO  main         o.f.core.internal.command.DbMigrate Current version of schema "public": << Empty Schema >>
07:04:08.065 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.1 - initial"
07:04:08.180 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.2 - worker heartbeat"
07:04:08.604 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.3 - worker heartbeat"
07:04:09.085 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.4 - postgres-queues-pkey"
07:04:09.901 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.5 - multitenant"
07:04:09.264 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.6 - multitenant on multipleconditions"
07:04:09.046 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.7 - execution queued"
07:04:09.464 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.8 - execution cancelled"
07:04:09.617 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.9 - execution queued"
07:04:09.161 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.10 - multitenant indices"
07:04:09.664 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.12 - execution triggerid"
07:04:09.853 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.13 - log fulltext"
07:04:09.107 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.14 - subflow executions"
07:04:09.510 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.15 - trigger store next date"
07:04:09.148 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.16 - log timestamp index"
07:04:09.303 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.17 - service instance"
07:04:09.033 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.18 - retry revamp"
07:04:09.200 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.19 - retry flow"
07:04:09.572 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.20 - drop worker instance"
07:04:09.472 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.21 - trigger worker id"
07:04:09.304 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.22 - flow with source"
07:04:09.754 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.23 - execution queued index"
07:04:09.013 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.24 - sla monitor"
07:04:09.430 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.25 - dashboard"
07:04:09.180 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.26 - skipped"
07:04:09.317 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.27 - escape fulltext"
07:04:09.206 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.28 - cluster event"
07:04:09.990 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.29 - subflow execution end"
07:04:09.684 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.30 - delete subflow executions"
07:04:09.402 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.31 - queues updated date"
07:04:09.953 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.32 - queues index on key"
07:04:09.360 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.34 - service instance indices"
07:04:09.341 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.35 - triggers index on next execution date"
07:04:09.552 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.36 - service instance index on service id"
07:04:09.195 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.37 - execution kind"
07:04:09.516 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.38 - flow interface"
07:04:09.292 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.39 - execution breakpoint"
07:04:09.205 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.41 - offset bigint"
07:04:09.601 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.43 - multiple condition event"
07:04:09.975 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.44 - concurrency-limit"
07:04:09.327 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.45 - taskrun submitted"
07:04:09.008 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.46 - kv metadata"
07:04:09.229 INFO  main         o.f.core.internal.command.DbMigrate Migrating schema "public" to version "1.47 - taskrun resubmitted"
07:04:09.229 INFO  main         o.f.core.internal.command.DbMigrate Successfully applied 43 migrations to schema "public", now at version v1.47 (execution time 00:00.193s)
07:04:10.058 INFO  main         i.kestra.core.plugins.PluginScanner Registered 102 core plugins (scan done in 130ms)
07:04:10.593 INFO  main         i.k.c.c.s.AbstractServerCommand Machine information: 16 available cpu(s), 3780MB max memory, Java version 21.0.9+10-LTS
07:04:10.093 INFO  standalone   io.kestra.cli.AbstractCommand Starting Kestra 1.1.14 with environments [cli] [revision 94be24d / 2026-01-13T14:55]
07:04:11.237 INFO  standalone   i.kestra.core.plugins.PluginScanner Registered 922 plugins from 165 groups (scan done in 472ms)
07:04:12.066 INFO  standalone   io.kestra.cli.AbstractCommand Server Running: http://ed13aee505d2:8080, Management server on port http://ed13aee505d2:8081/health
07:04:13.073 INFO  standalone   i.k.w.services.FlowAutoLoaderService Loaded 6 "Getting Started" flows from community blueprints. You can disable this feature by setting 'kestra.tutorialFlows.enabled=false'.
07:04:13.965 INFO  standalone-runner_1 io.kestra.worker.DefaultWorker Worker started with 128 thread(s)
07:04:13.602 INFO  standalone-runner_0 io.kestra.jdbc.runner.JdbcExecutor Executor started with 16 thread(s)
07:04:13.048 INFO  standalone-runner_3 io.kestra.jdbc.runner.JdbcIndexer Indexer started
07:04:13.196 INFO  standalone-runner_2 i.kestra.scheduler.AbstractScheduler Scheduler started
07:04:40.697 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:40.455Z | GET / HTTP/1.1 | status: 307 | ip: 172.18.0.1 | length: - | duration: 38
07:04:40.127 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:40.499Z | GET /ui/ HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 1225 | duration: 76
07:04:41.422 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:40.909Z | GET /api/v1/configs HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 496 | duration: 360
07:04:41.474 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:41.275Z | GET /api/v1/basicAuthValidationErrors HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 114 | duration: 7
07:04:41.031 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:41.294Z | GET /api/v1/configs HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 496 | duration: 3
07:04:41.929 INFO  default-nioEventLoopGroup-1-12 io.kestra.webserver.access 2026-01-24T07:04:41.302Z | GET /api/v1/basicAuthValidationErrors HTTP/1.1 | status: 200 | ip: 172.18.0.1 | length: 114 | duration: 3