
class constOpt:
	def __init__(self, f,ip, ss, lr, tol):
		super()
	#define arg
		self.f=f
		self.ip=ip
		self.tol=tol
		self.ss=ss
		self.lr=lr
	#define internal parser
		self.fval1=0
		self.fval2=0
		self.df=0
		self.np=[]
		self.initial()
		self.count=0
	
	def initial(self):
		# this function intiailize the first step of the solver
		self.fval1=self.f(*self.ip)
		for _ in self.ip:
			self.np.append(_+self.ss)
		self.fval2=self.f(*self.np)
		self.df=-(self.fval2-self.fval1)
		for i in range(0,self.ip.__len__()):
			self.np[i]=self.ip[i]-self.lr*(self.df)/(self.ss)
		
	def solvestep(self):
		# this is the inner function that is being called by the solver
		self.fval1=self.f(*self.ip)
		self.fval2=self.f(*self.np)
		self.df=-(self.fval2-self.fval1)
		temp=self.np
		for i in range(0,self.ip.__len__()):
			#self.np[i]=self.ip[i]-self.lr*(self.df)/(self.np[i]-self.ip[i])
			self.np[i]=self.ip[i]-self.lr*(self.df)
		self.ip=temp
		
	
	def solve(self):
		# this is the main solve function being called by user
		while(self.df>self.tol):
			print(self.df)
			self.solvestep()
			self.count+=1
		return self.count, self.f(*self.np), self.np
		
		
				
if __name__=="__main__":
	def q(a):
		return (a+5)*(a+5)
	
	opt=constOpt(q,[50],50,0.5,0.000000000000000001)
	answer=opt.solve()
	print(answer)
	
	
	
	
	