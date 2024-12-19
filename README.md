# AI Image Studio

A full-stack AI image generation application using Stable Diffusion XL, FastAPI, and React. Create AI-generated images through a modern web interface with secure authentication.

## Project Structure
```
.
├── backend/          # FastAPI application with JWT auth & AI integration
├── frontend/         # Vite React application with modern UI
├── docker-compose.yml
└── k8s/              # Kubernetes configuration files
```

## Features
- AI Image Generation using Stable Diffusion XL
- Secure JWT authentication
- Modern React frontend with Tailwind CSS
- FastAPI backend for high performance
- Docker Compose setup for easy development
- PostgreSQL database for user management
- Fast development with Vite
- Kubernetes deployment ready

## Prerequisites
- Docker and Docker Compose
- Node.js 18+
- Python 3.12+
- Poetry (for backend development)
- kubectl (for Kubernetes deployment)
- Hugging Face API token

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/stephen-a-nicholson/simple-webapp-k8s.git
cd ai-image-studio
```

2. Create `.env` file in the root directory:
```
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=your_db_name
SECRET_KEY=your_jwt_secret_key
HUGGINGFACE_API_TOKEN=your_huggingface_token
```

3. Start the application:
```bash
docker compose up -d
```

4. Access the application:
- Web Interface: http://localhost:5173
- API Documentation: http://localhost:8000/docs

## Development

### Backend Development
The backend uses FastAPI with the following features:
- JWT authentication
- Hugging Face Stable Diffusion XL integration
- PostgreSQL database
- Poetry for dependency management

See [backend/README.md](./backend/README.md) for detailed backend documentation.

### Frontend Development
The frontend is built with:
- Vite & React
- TypeScript for type safety
- Tailwind CSS for styling
- Modern, responsive design

To develop locally:
```bash
cd frontend
npm install
npm run dev
```

## Docker Services
- `frontend`: Vite React application
- `backend`: FastAPI application
- `db`: PostgreSQL database

## API Endpoints
- `POST /token`: Authentication endpoint
- `POST /image/generate`: Generate images (protected)
- `GET /health`: Health check endpoint

## Environment Variables
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `SECRET_KEY`: JWT secret key
- `HUGGINGFACE_API_TOKEN`: Hugging Face API token for image generation

## Production Deployment

### Using Kubernetes
1. Build and push Docker images to your registry
2. Update Kubernetes manifests in `k8s/` directory
3. Apply configurations:
```bash
kubectl apply -f k8s/
```

## Security Considerations
- Secure storage of Hugging Face API tokens
- Rate limiting for image generation
- Proper CORS configuration
- SSL/TLS in production
- Regular security audits
- Secure password policies

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request