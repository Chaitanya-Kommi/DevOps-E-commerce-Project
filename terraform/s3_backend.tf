terraform {
  backend "s3" {
    bucket       = "terraform-statefile-190535468276-eu-west-2-an"
    key          = "terraform.tfstate"
    region       = "eu-west-2"
    encrypt      = true
    use_lockfile = true
  }
}