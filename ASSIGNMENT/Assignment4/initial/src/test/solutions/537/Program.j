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
Label0:
	iconst_0
	ifle Label2
Label4:
	ldc "Yes"
	invokestatic io/putString(Ljava/lang/String;)V
Label5:
	goto Label3
Label2:
	iconst_1
	ifle Label6
Label8:
	ldc "In Scope Else if"
	invokestatic io/putString(Ljava/lang/String;)V
Label9:
	goto Label7
Label6:
Label10:
	ldc "No"
	invokestatic io/putString(Ljava/lang/String;)V
Label11:
Label7:
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
