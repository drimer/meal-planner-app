resource "aws_s3_bucket" "frontend" {
  bucket = "meal-planner-frontend"
  acl    = "public-read"
}

resource "aws_s3_bucket_object" "frontend_files" {
  for_each = fileset("../frontend/build/web", "**")

  bucket = aws_s3_bucket.frontend.bucket
  key    = each.key
  source = "../frontend/build/web/${each.key}"
  acl    = "public-read"
}