s1 = "spam\n"   # \n \r \t \f \b
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print(type(s1), len(s1))
print('Guido is the "BDFL" emeritus')
print("Guido's the BDFL emeritus")

print("""Guido's the "BDFL" emeritus "" of Python""")

query = """
select *
from dot_reports
where zip_code = '20383'
"""

s5 = r"spam\n"
print(s5)

print("foo\n", r"foo\n")


