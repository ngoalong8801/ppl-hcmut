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
.var 1 is num Z from Label0 to Label1
Label0:
.var 2 is num Z from Label0 to Label1
	iconst_1
	istore_1
	iload_1
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method
