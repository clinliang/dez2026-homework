# 1. Enable APIs via Terraform
resource "google_project_service" "gcp_services" {
  for_each = toset(var.gcp_service_list)
  project  = var.project
  service  = each.key

  # IMPORTANT: Prevents accidental disabling of APIs when you delete infrastructure
  disable_on_destroy = false 
}

# 2. Create the Bucket (Wait for the API to be ready!)
resource "google_storage_bucket" "taxi_bucket" {
  name          = var.gcs_bucket_name
  location      = var.region
  force_destroy = true 

  depends_on = [google_project_service.gcp_services]
}

# 3. Create BigQuery Dataset
resource "google_bigquery_dataset" "taxi_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.region

  depends_on = [google_project_service.gcp_services]
}

# 4. Create the External Table (Metadata only)
resource "google_bigquery_table" "external_yellow_taxi" {
  dataset_id = google_bigquery_dataset.taxi_dataset.dataset_id
  table_id   = "external_yellow_tripdata"

  # This is the key fix:
  deletion_protection = false

  external_data_configuration {
    autodetect    = true
    source_format = "PARQUET"
    source_uris   = ["gs://${google_storage_bucket.taxi_bucket.name}/yellow_tripdata_*.parquet"]

    # Add this to handle the "empty bucket" during first run
    ignore_unknown_values = true
  }
}