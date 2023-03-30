import os
import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'app:Service',
        reload=True,
        factory=True,
        host=os.getenv('API_HOST', '0.0.0.0'),
        port=int(os.getenv('API_PORT', 5000)),
        log_level='debug',
        lifespan='on'
    )