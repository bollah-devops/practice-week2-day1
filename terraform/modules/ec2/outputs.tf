output "app_public_ip" {
  value = aws_instance.blog_platform_server.public_ip
}

output "app_instance_id" {
  value = aws_instance.blog_platform_server.id
}
