FROM golang:alpine AS builder

LABEL stage=gobuilder

ENV CGO_ENABLED=0
ENV GOOS=linux

RUN apk update --no-cache && apk add --no-cache tzdata

WORKDIR /build

ADD go.mod .
ADD go.sum .

RUN go mod download

COPY . .

RUN go build -o /app/main ./main.go

FROM alpine

RUN apk update --no-cache && apk add --no-cache ca-certificates

COPY --from=builder /usr/share/zoneinfo/Europe/Moscow /usr/share/zoneinfo/Europe/Moscow
ENV TZ=Europe/Moscow

WORKDIR /app

COPY --from=builder /app/main /app/main

CMD ["./main"]