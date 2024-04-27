from shortner.unique_id_generator.gen_twitter_snowflake_id import Snowflake
from shortner.unique_id_generator.to_base_62 import to_base62

class IdGenerator:

    def __init__(self):
        """        Initialize the instance of the class.

        This method initializes the instance of the class and sets the _id attribute to None.

        Args:
            self: The instance of the class.
        """

        self._id = None
    
    def generate_id(self):
        """        Generate a short unique identifier using Snowflake algorithm and base62 encoding.

        This function generates a unique identifier using the Snowflake algorithm with a worker_id of 10,
        then converts the generated identifier to a base62 encoded string.

        Returns:
            str: A short unique identifier.
        """

        snowflake = Snowflake(worker_id=10)
        val = snowflake.generate_id()
        short_code = to_base62(val)
        return short_code