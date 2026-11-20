# Historical Incident: Elevated API Latency From Database Queries

## Summary
Product Catalog API latency increased while error rates remained relatively low.

## Impact
Product pages and catalog requests became slow.

## Detection
p95 and p99 latency increased significantly.

## Investigation
Distributed traces showed database queries consuming most of the request time. Database monitoring showed increased query latency.

## Root Cause
A query pattern introduced by a catalog feature caused inefficient database access at higher traffic volume.

## Resolution
The query behavior was corrected and database performance returned to normal.

## Lessons Learned
Average latency can hide tail-latency incidents. p95/p99 metrics and traces should be part of routine monitoring.

Related:
- `10_high_latency_incident_runbook.md`
- `03_product_catalog_api.md`
- `07_data_storage_and_cache_architecture.md`
