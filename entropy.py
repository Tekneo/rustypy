import rustypy 
import time
with open('testdata.bin', 'rb') as f: 
	DATA = f.read()
start=time.perf_counter() 
rustypy.compute_entropy_pure_python(DATA)
end=time.perf_counter()
print((end-start)*10000)

start=time.perf_counter() 
rustypy.compute_entropy_scipy_numpy(DATA)
end=time.perf_counter()
print((end-start)*10000)

start=time.perf_counter() 
rustypy.compute_entropy_rust_from_python(DATA)
end=time.perf_counter()
print((end-start)*10000)
