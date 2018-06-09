non-official instagram API server
===

##Quick start

`docker run --rm -it -p 8842:8842 -v {path-to-thsi-dir}:/home/scraper instascraper:test python3 test.py`

## API

### /posts
Get post'ss rough information.

#### Request

##### Query parameter

- hashtag: String

##### Body
None

#### Response

##### Body
```json
{
  "image_url": "hoge",
  "post_id": "hoge,
}
```

### /posts/{post_id}
Get post's detail information.

#### Request

##### Query parameter
None

##### Body
None

#### Response

##### Body

```json
{
  "user_name": "hoge",
}
```
