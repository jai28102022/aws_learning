curl --location --request GET 'https://00hp2n9h67.execute-api.ap-south-1.amazonaws.com/prod'

curl --location --request POST 'https://00hp2n9h67.execute-api.ap-south-1.amazonaws.com/prod' \
--header 'Content-Type: application/json' \
--data-raw '{
    "userid": "6",
    "username": "demo006"
}'

curl --location --request PATCH 'https://00hp2n9h67.execute-api.ap-south-1.amazonaws.com/prod' \
--header 'Content-Type: application/json' \
--data-raw '{
    "userid": "3",
    "username": "demo003"
}'

curl --location --request DELETE 'https://00hp2n9h67.execute-api.ap-south-1.amazonaws.com/prod' \
--header 'Content-Type: application/json' \
--data-raw '{
    "userid": "3"
}'
