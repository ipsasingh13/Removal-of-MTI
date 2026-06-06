# Deployment Guide

## Docker
docker build -t mti-project .
docker run -p 5000:5000 mti-project

## Render
1. Push project to GitHub.
2. Create a new Web Service in Render.
3. Render will automatically detect render.yaml.
4. Deploy.

## Vercel
1. Push repository to GitHub.
2. Import project into Vercel.
3. Vercel will use vercel.json.
4. Deploy frontend.
