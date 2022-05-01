from django import forms


from .models import Employee ,Teams

class EmployeeForm(forms.ModelForm):
    class Meta:
      model = Employee
      fields = ['name','teams']
      widges ={
          'name':forms.TextInput(attrs={'class':"py-3 px-3 mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"}),
          'teams':forms.Select(attrs={'class':"py-3 px-3 mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"})
      }

class TeamsForm(forms.ModelForm):
    class Meta:
      model = Teams
      fields = ['teamCategure','teamDescription']
      widges ={
          'teamCategure':forms.TextInput(attrs={'class':"py-3 px-3 mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"}),
          'teamDescription':forms.Textarea(attrs={'class':"py-3 px-3 mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"})
      }
