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
.var 1 is check F from Label0 to Label1
Label0:
	iconst_0
	i2f
	fstore_1
	fload_1
	iconst_1
	i2f
	fadd
	fstore_1
	fload_1
	iconst_2
	i2f
	fmul
	ldc 2.56
	fadd
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
