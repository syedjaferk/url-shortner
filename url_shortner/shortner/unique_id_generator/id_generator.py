from shortner.unique_id_generator.gen_twitter_snowflake_id import Snowflake
from shortner.unique_id_generator.to_base_62 import to_base62

class IdGenerator:

    def __init__(self):
        self._id = None
    
    def generate_id(self):
        snowflake = Snowflake(worker_id=10)
        val = snowflake.generate_id()
        short_code = to_base62(val)
        return short_code