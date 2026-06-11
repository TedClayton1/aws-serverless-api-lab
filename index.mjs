export const handler = async (event) => {
  console.log("Incoming event:", JSON.stringify(event));

  const params = event.queryStringParameters || {};
  const name = params.name || "Unknown";

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: `HELLO ${name.toUpperCase()} FROM NODE!`
    })
  };
};