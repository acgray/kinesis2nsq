# kinesis2nsq

A very simple bridge to forward messages from Kinesis to NSQ using AWS Lambda.

## Usage

Deploy to AWS by running:

```
KINESIS_STREAM_ARN=arn:aws:..... serverless deploy
```

You can also build the package and do something with it manually (e.g. as part
of an external build process) using `serverless package`.