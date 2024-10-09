
def generate_link(number:int , nationaity:str):
    """Generate a link to the ticket details page
    
    Args:
        number (int): The ticket number
        nationaity (str): The nationaity of the ticket holder
        
    Returns:
        str: The link to the ticket details page in markdown format
    """
    return f"[Link](http://localhost:5000/?number_of_people={int(number)}&nationality={nationaity})"
    

