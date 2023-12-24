from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-LrQXxXQLrhtBCoqFQE534K7y", 
  model="gpt-3.5-turbo"
)