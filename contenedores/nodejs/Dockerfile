FROM node:16-alpine

WORKDIR /code

COPY package*.json ./

RUN npm install

COPY . ./

EXPOSE 3000

CMD [ "node", "servidor_node.js" ]