Task Overview
You are working on a FastAPI-based API service that manages customer support tickets. The /tickets endpoint has stopped applying pagination and status filtering, causing all tickets to be returned for every request. This is affecting internal and external teams relying on paginated, filtered data.

Guidance
Focus on restoring the correct pagination and filtering behavior for the endpoint while keeping the current authentication mechanism untouched. The project is containerized and can be interacted with through the provided Docker infrastructure. The ticket dataset is mocked for testing purposes.

Objectives
Restore the ability of the /tickets endpoint to accept and correctly handle 'limit', 'offset', and 'status' query parameters so that results are paginated and can be filtered by ticket status. Ensure only the relevant, requested subset of tickets is returned per API call.

How to Verify
Submit API requests with various combinations of 'limit', 'offset', and 'status' query parameters to the running service. Confirm that each response contains only the expected set of tickets as specified by the request parameters.