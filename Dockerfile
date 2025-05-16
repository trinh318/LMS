# Sử dụng openjdk 21 làm base image
FROM openjdk:21-jdk-slim

# Chỉ định thư mục làm việc trong container
WORKDIR /app

# Sao chép file JAR vào thư mục làm việc
COPY target/hcm25_cpl_ks_java_01_lms-0.0.1-SNAPSHOT.jar app.jar

# Mở cổng cho ứng dụng
EXPOSE 8080

# Lệnh để chạy ứng dụng
ENTRYPOINT ["java", "-jar", "app.jar"]