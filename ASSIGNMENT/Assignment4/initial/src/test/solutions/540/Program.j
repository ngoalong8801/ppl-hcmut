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
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_4
	istore_1
	iconst_5
	istore_2
	iload_1
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	ldc "Yes"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
	goto Label5
Label4:
	iconst_4
	iload_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iload_2
	iconst_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iand
	ifle Label12
Label14:
	ldc "In Scope Else if"
	invokestatic io/putString(Ljava/lang/String;)V
Label15:
	goto Label13
Label12:
Label16:
	ldc "No"
	invokestatic io/putString(Ljava/lang/String;)V
Label17:
Label13:
Label5:
	ldc "EndIF"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
.limit locals 3
.end method
