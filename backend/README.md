# simple-webapp-k8s

A secure FastAPI application using Poetry for dependency management and Kubernetes for deployment, featuring JWT authentication.

## Features
- FastAPI web framework with JWT authentication
- Poetry dependency management
- Gunicorn with Uvicorn workers
- Security headers and CORS configuration
- Kubernetes deployment configuration
- Health check endpoint
- Protected endpoints with JWT tokens

## Local Development

### Prerequisites
- Docker
- Poetry
- Kubernetes cluster (e.g., minikube)
- kubectl

### Building and Running Locally

1. Install dependencies:
```bash
poetry install
```

2. Build the Docker image:
```bash
# For production build
docker build -t hello-world-api:latest .

# For development build (includes dev dependencies)
docker build -t hello-world-api:dev --build-arg INSTALL_DEV=true .
```

3. Run the container:
```bash
docker run -p 8000:8000 hello-world-api:latest
```

### Testing Authentication

1. Access the Swagger UI at `http://localhost:8000/docs`

2. Get JWT Token:
   - Click on `/token` endpoint
   - Click "Try it out"
   - Use test credentials:
     ```
     username: testuser
     password: password123
     ```
   - Execute and copy the access token

3. Authorise Protected Endpoints:
   - Click the "Authorise" button (lock icon) at the top
   - Enter: `Bearer <your-access-token>`
   - Click "Authorise"
   - Now you can access protected endpoints

### Kubernetes Deployment with Minikube

1. Start Minikube and set up environment:
```bash
# Start Minikube
minikube start

# Point Docker CLI to Minikube's Docker daemon
eval $(minikube docker-env)

# Build image in Minikube's context
docker build -t hello-world-api:latest .
```

2. Apply Kubernetes manifests:
```bash
kubectl apply -f k8s/
```

3. Monitor deployment:
```bash
# Check pod status
kubectl get pods

# Check logs
kubectl logs -l app=hello-world-api

# Check service
kubectl get services
```

4. Access the application:
```bash
# Get service URL
minikube service hello-world-api --url

# Or use port forwarding
kubectl port-forward service/hello-world-api 8000:8000
```

5. Troubleshooting:
```bash
# Check detailed pod status
kubectl describe pods

# Check endpoints
kubectl get endpoints hello-world-api

# Delete and redeploy
kubectl delete -f k8s/
kubectl apply -f k8s/
```

## API Endpoints

- `POST /token`: Get JWT token (authentication)
- `GET /`: Returns hello world message (protected)
- `GET /health`: Health check endpoint (public)

## Security Features
- JWT token authentication
- Non-root user execution
- Security headers
- Resource limits
- ReadOnly root filesystem
- No privilege escalation
- Health checks
- CORS configuration
- Password hashing with bcrypt

## Important Notes

1. For local testing:
   - Always build images in Minikube's Docker context
   - Use `imagePullPolicy: Never` in deployment
   - Ensure Minikube has enough resources

2. Authentication:
   - Store production secrets securely (not in code)
   - Update CORS settings for production
   - Use strong passwords and proper user management

3. Production Deployment:
   - Update resource limits based on actual usage
   - Configure proper ingress/load balancing
   - Set up monitoring and logging
   - Use proper secrets management