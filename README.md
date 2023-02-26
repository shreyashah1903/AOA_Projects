# AOA_Projects
Projects for Analysis of Algorithms class - Spring 2023

# Access the Thunder server
1. Visit https://register.cise.ufl.edu/ to register for server access. Gets approved within 5 mins(Follow this
link for steps : https://it.cise.ufl.edu/support/account-creation-and-management/)
2. SSH to the server using
```
ssh siju.sakaria@thunder.cise.ufl.edu
```
3. Enter your `Gatorlink` password
4. In a new terminal tab, copy the project files from your machine to the server using
```
scp -r * siju.sakaria@thunder.cise.ufl.edu:/cise/homes/siju.sakaria
```
5. Run the makefile on the server using `make run #`(# can be tasks 1-5)
6. Provide the input `n m` (days, houses) and the houses availability
7. Output would be indices of houses which will be painted