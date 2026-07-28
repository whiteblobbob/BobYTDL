FROM node:22-alpine AS builder

WORKDIR /app

# install deps
COPY package.json .
RUN npm install

# build deployed app
COPY . .
RUN npm run build

FROM nginx:alpine

# grabs build result folder and puts it inside nginx html folder
COPY --from=builder /app/dist /usr/share/nginx/html

# exposes port, a port can be defined to "connect" to this port on runtime
EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]