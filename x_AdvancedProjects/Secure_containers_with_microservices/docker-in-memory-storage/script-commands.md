# Docker In-Memory Storage Command Reference Guide

- [Section 1: Container Operations](#section-1-container-operations)
- [Section 2: tmpfs Mount Management](#section-2-tmpfs-mount-management)
- [Section 3: Docker Build and Run](#section-3-docker-build-and-run)
- [Section 4: Monitoring and Inspection](#section-4-monitoring-and-inspection)
- [Section 5: Maintenance Operations](#section-5-maintenance-operations)

> **Author**: mchyasn  
> **Description**: Reference guide for Docker in-memory storage implementation  
> **Learning Focus**: Docker containerization, tmpfs mounts, and security  
> **Note**: This is a reference guide. Do not execute commands without understanding their implications.

## Section 1: Container Operations

### Basic Container Management
```bash
# List running containers
docker ps

# List all containers including stopped ones
docker ps -a

# Stop a running container
docker stop <container_id>

# Remove a container
docker rm <container_id>
```

### Container Cleanup
```bash
# Remove all stopped containers
docker container prune

# Remove all unused containers, networks, and images
docker system prune -a
```

## Section 2: tmpfs Mount Management

### Basic tmpfs Mount
```bash
# Mount tmpfs to container
docker run --rm \
    --mount type=tmpfs,dst=/tmp \
    alpine:latest

# Mount tmpfs with size limit
docker run --rm \
    --mount type=tmpfs,dst=/app/tmp,tmpfs-size=16k \
    alpine:latest
```

### Advanced Mount Configuration
```bash
# Mount with specific permissions
docker run --rm \
    --mount type=tmpfs,dst=/app/tmp,tmpfs-size=16k,tmpfs-mode=1770 \
    alpine:latest

# Mount multiple tmpfs locations
docker run --rm \
    --mount type=tmpfs,dst=/app/tmp1,tmpfs-size=16k \
    --mount type=tmpfs,dst=/app/tmp2,tmpfs-size=16k \
    alpine:latest
```

## Section 3: Docker Build and Run

### Image Building
```bash
# Build Docker image
docker build -t my_microservice .

# Build with no cache
docker build --no-cache -t my_microservice .

# Build with specific Python version
docker build --build-arg PYTHON_VERSION=3.9 -t my_microservice .
```

### Container Running
```bash
# Run container with tmpfs
docker run --rm -d \
    --mount type=tmpfs,dst=/app/tmp,tmpfs-size=16k,tmpfs-mode=1770 \
    my_microservice

# Run with environment variables
docker run --rm -d \
    --mount type=tmpfs,dst=/app/tmp \
    -e DEBUG=1 \
    my_microservice
```

## Section 4: Monitoring and Inspection

### Container Inspection
```bash
# Inspect container mounts
docker inspect <container_id>

# View container logs
docker logs <container_id>

# Follow container logs
docker logs -f <container_id>
```

### Resource Monitoring
```bash
# View container resource usage
docker stats <container_id>

# Execute commands in container
docker exec -it <container_id> /bin/bash
```

## Section 5: Maintenance Operations

### Image Management
```bash
# List images
docker images

# Remove image
docker rmi my_microservice

# Clean up dangling images
docker image prune
```

### Volume Management
```bash
# List volumes
docker volume ls

# Remove unused volumes
docker volume prune
```

## Learning Notes

1. Always verify tmpfs mount configuration before running sensitive operations
2. Monitor container memory usage when using tmpfs mounts
3. Implement proper error handling for file operations in tmpfs
4. Consider security implications of mount permissions
5. Regular cleanup of unused resources is essential

---

>  **Best Practice**: Always specify tmpfs size limits to prevent memory exhaustion

> ⚠️ **Warning**: tmpfs data is lost when container stops - ensure proper data handling

>**Note**: Mount points are isolated between containers even with same path

# Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Python Documentation](https://docs.python.org/)
- [Container Security Best Practices](https://docs.docker.com/develop/security-best-practices/)