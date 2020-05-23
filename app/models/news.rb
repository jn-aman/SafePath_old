class News < ApplicationRecord
    def self.new_update
        `python new_crimes.py`
        `python ruby_python.py`
 
    end
end
