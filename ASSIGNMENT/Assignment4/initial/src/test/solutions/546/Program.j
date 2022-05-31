.source Program.java
.class public Program
.super java.lang.Object

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_1
	istore_2
Label2:
	iload_1
	iconst_0
	if_icmplt Label3
	iload_1
	iconst_2
	if_icmpgt Label3
Label6:
Label8:
	iload_2
	iconst_1
	if_icmplt Label9
	iload_2
	iconst_2
	if_icmpgt Label9
Label12:
	ldc "Hello World"
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
Label11:
Label7:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 3
.limit locals 3
.end method
