
<hr>

The self-explanatory part of processing replies and delivering outputs. 

Here is a sample internal dialogue of the model for ease :

```mermaid
flowchart TD
    A[The user is asking if the store sells TVs. Specific product category] --> B(The user is not asking about a specific product but about a product category TVs)
    B --> C(Therefore, we cannot identify if the specific product is available or not)
    C -->|Response to user| D[Response to user: We apologize, but we cannot provide a specific answer regarding the availability of TVs.]
    D --> E[Is there anything else we can assist you with?]


  
```

--- 
For our convenience, we find it easier to mask the thoughts and reply to a simple dialogue for our answer. 

The codes are marked with comments as well to understand. 
