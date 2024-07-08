

def testing():
  print("pkg2A is successfully imported")


#No whitespace inside parentheses, brackets or braces.

#wrong
spam( ham[ 1 ], { 'eggs': 2 }, [ ] ) 

#correct
spam(ham[1], {'eggs': 2}, []) 

#No whitespace before a comma, semicolon, or colon. Do use whitespace after a comma, semicolon, or colon, except at the end of the line.
#correct
if x == 4:
        print(x, y)
        x, y = y, x


def calculate_area(length: float, width: float = 1.0) -> float:
    """Calculate the area of a rectangle."""

    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")

    area = length * width  
    return area  


def print_area(length, width=1.0):
    """Print the area of a rectangle."""
    area = calculate_area(length, width)  # No blank line after def line; no spaces around '=' for keyword arguments
    print(f"The area is {area}")  # No whitespace before open parenthesis


class Rectangle:
    """A class to represent a rectangle."""

    def __init__(self, length: float, width: float = 1.0):
        self.length = length  # No whitespace before open parenthesis; spaces around '=' for assignment
        self.width = width  # Spaces around '=' for assignment

    def area(self) -> float:
        return self.length * self.width  # Single spaces around binary operator '*'

    def is_square(self) -> bool:
        return self.length == self.width  # Single spaces around comparison '=='

    def display_info(self):
        if self.is_square():
            print("This rectangle is a square.")  # No whitespace before open parenthesis
        else:
            print("This rectangle is not a square.")  # No whitespace before open parenthesis

        print(f"Area: {self.area()}")  # No whitespace before open parenthesis


# Instantiate a Rectangle object and display its information
rect = Rectangle(length=5, width=5)  # No spaces around '=' in argument list; no whitespace before open parenthesis
rect.display_info()  # No whitespace before open parenthesis

# Demonstrate proper use of indexing and function calls
numbers = [1, 2, 3, 4, 5]  # No spaces around '=' for assignment and space after , and no space before ,
print(numbers[2])  # No whitespace before open bracket
result = calculate_area(3, 4)  # No whitespace before open parenthesis
print(f"Calculated area: {result}")  # No whitespace before open parenthesis





# A docstring is mandatory for every function that has one or more of the following properties:

# being part of the public API -(used by the public)
# nontrivial size -(huge piece of code)
# non-obvious logic -(tricky logic)

#example

def calculate_discount(price, customer_type):
    """
    Calculate the discount based on price and customer type.
    
    This function applies different discount rates depending on whether the
    customer is a regular, premium, or VIP member. The discount logic takes
    into account various business rules and seasonal promotions.
    """
    # Function logic here

def fetch_smalltable_rows(
    table_handle: smalltable.Table,
    keys: Sequence[bytes | str],
    require_all_keys: bool = False,
) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
          returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """

#class is similar to func
class SampleClass:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Initializes the instance based on spam preference.

        Args:
          likes_spam: Defines if instance exhibits this preference.
        """
        self.likes_spam = likes_spam
        self.eggs = 0

    @property
    def butter_sticks(self) -> int:
        """The number of butter sticks we have."""

#inline comments
        
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.
i=0
if i & (i-1) == 0:  # True if i is 0 or a power of 2.
    print("hiiii")
#To improve legibility, these comments should start at least 2 
#spaces away from the code with the comment character #, followed by at least one space before the text of the comment itself.
  