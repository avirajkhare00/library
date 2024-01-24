FROM node:21-alpine

WORKDIR /app/library-frontend/

COPY package*.json /app/library-frontend/
RUN npm install

COPY . /app/library-frontend/

CMD ["npm", "start"]

