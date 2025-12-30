from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP(
    name="math", # only used for SSE transport (set this to any port)
    # stateless_http=True,
)

@mcp.tool()
def add(a: float, b: float) -> float:
    #the part that define the function is really important, do not skip it.  
    """calculate and returns the sum of two numbers. 
    """
    print(f"Server received add request: {a}, {b}")
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """calculate and returns the difference of two numbers. 
    """
    print(f"Server received subtract request: {a}, {b}")
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:  
    """calculate and returns the product of two numbers. 
    """
    print(f"Server received multiply request: {a}, {b}")
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:        
    """calculate and returns the quotient of two numbers. 
    """
    print(f"Server received divide request: {a}, {b}")
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

@mcp.tool()
def sine(a: float) -> float:
    """calculate and returns the sine of a number."""
    print(f"Server received sine request: {a}")
    return math.sin(a)


@mcp.tool()
def sine(a: float) -> float:
    """calculate and returns the sine of a number."""
    print(f"Server received sine request: {a}")
    return math.sin(a)

@mcp.tool()
def cosine(a: float) -> float:
    """calculate and returns the cosine of a number."""
    print(f"Server received cosine request: {a}")
    return math.cos(a)  

@mcp.tool()
def tangent(a: float) -> float:
    """calculate and returns the tangent of a number."""
    print(f"Server received tangent request: {a}")
    return math.tan(a)  

if __name__ == "__main__":
    mcp.run(transport="stdio") 

