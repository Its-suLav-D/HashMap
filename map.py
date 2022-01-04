class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)                        # The returned hash code will be the bucket_index
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)                          # length of array to be used in Mod operation
        
        current_coefficient = 1                                       # represents (self.p^0) which is 1
        
        hash_code = 0
        
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code (Mod operation)
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient as well

        return hash_code % num_buckets                                # one last compression before returning
    
    
    def size(self):
        return self.num_entries

hash_map = HashMap()
bucket_index = hash_map.get_bucket_index('abcd')
print(bucket_index) 

bucket_index = hash_map.get_bucket_index('bcda')
print(bucket_index)