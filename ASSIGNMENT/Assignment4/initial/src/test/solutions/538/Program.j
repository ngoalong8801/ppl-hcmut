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
.var 1 is check Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	ifgt Label2
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
	iload_1
	ifle Label8
Label10:
	ldc "In Scope Else if"
	invokestatic io/putString(Ljava/lang/String;)V
Label11:
	goto Label9
Label8:
Label12:
	ldc "No"
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
Label9:
Label5:
	ldc "EndIF"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
