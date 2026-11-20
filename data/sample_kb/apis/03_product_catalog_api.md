# Product Catalog API

## Base Path

`/api/v1/products`

## Get Product

`GET /api/v1/products/{product_id}`

Returns product details.

Possible responses:
- `200` product found
- `404` product not found
- `500` internal error
- `503` dependency unavailable

## List Products

`GET /api/v1/products`

Common query parameters:

- `q`
- `category`
- `page`
- `limit`

Possible responses:
- `200` successful list
- `400` invalid query
- `429` rate limit
- `500` internal error
- `503` dependency unavailable

## Dependencies

- PostgreSQL
- Redis where caching is enabled
- API Gateway

## Investigation

For increased product latency:

1. compare cache hit rate
2. inspect Redis latency/errors
3. inspect database query latency
4. check connection pool usage
5. inspect recent catalog changes
6. compare current traffic with baseline

For a product `404`, verify the product ID and whether the product exists in the authoritative catalog data before treating it as a service incident.

Related documents:
- `07_data_storage_and_cache_architecture.md`
- `01_api_gateway.md`
