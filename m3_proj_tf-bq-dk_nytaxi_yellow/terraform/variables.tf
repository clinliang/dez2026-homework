variable "project" {
  description = "The unique ID of the GCP Project"
  default     = "nytaxi-yellow-cll"
}

variable "region" {
  description = "The geographic location for GCS and BigQuery"
  default     = "europe-west9"
}

variable "gcs_bucket_name" {
  description = "Name of the GCS Data Lake"
  default     = "m3-nytaxi-yellow-bucket"
}

variable "bq_dataset_name" {
  description = "Name of the BigQuery Dataset"
  default     = "m3_nytaxi_yellow_bq"
}

# Declare the APIs for pipeline needs
variable "gcp_service_list" {
  description = "The list of APIs necessary for the project"
  type        = list(string)
  default     = [
    "storage.googleapis.com",
    "bigquery.googleapis.com",
  ]
}