# Full Stack Authentication Demo

A full-stack application demonstrating secure authentication using FastAPI, Vite React, and PostgreSQL, with Docker Compose for local development and Kubernetes for deployment.

## Project Structure
```
.
├── backend/          # FastAPI application with JWT authentication
├── frontend/         # Vite React application
├── docker-compose.yml
└── k8s/              # Kubernetes configuration files
```

## Features
- FastAPI backend with JWT authentication
- Vite React frontend
- PostgreSQL database for user management
- Docker Compose setup for development
- Kubernetes deployment configuration
- Secure password handling
- Protected API endpoints

## Prerequisites
- Docker and Docker Compose
- Node.js 18+
- Python 3.12+
- Poetry (for backend development)
- kubectl (for Kubernetes deployment)

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create `.env` file in the root directory:
```
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=your_db_name
SECRET_KEY=your_jwt_secret_key
```

3. Start the application:
```bash
docker compose up -d
```

4. Access the applications:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Development

### Backend Development
See [backend/README.md](./backend/README.md) for detailed backend documentation.

### Frontend Development
The frontend is a Vite React application. To develop locally:

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

## Docker Compose Services

- `frontend`: Vite React application
- `backend`: FastAPI application
- `db`: PostgreSQL database

## Production Deployment

### Using Kubernetes
1. Build and push Docker images to your registry
2. Update Kubernetes manifests in `k8s/` directory
3. Apply configurations:
```bash
kubectl apply -f k8s/
```

See individual service READMEs for detailed deployment instructions.

## Security Considerations
- Store production secrets securely
- Update CORS settings for production
- Use proper SSL/TLS certificates
- Implement rate limiting
- Regular security audits
- Proper password policies

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request