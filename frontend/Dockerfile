# Stage 1: Build the React app
FROM node:16 AS build

WORKDIR /app

# Install dependencies
COPY app/package.json ./
RUN npm install

# Copy the rest of the application code
COPY app/ .

# Build the React app
RUN npm run build

# Stage 2: Serve the React app with Nginx
FROM nginx:alpine

# Copy the build output to the Nginx html directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
