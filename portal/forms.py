from django import forms


class CreateTestForm(forms.Form):
    test_name = forms.CharField(widget=forms.TextInput
                                (attrs={'class': 'border-b-2 mb-4 text-[17px] hover:border-slate-500 focus:border-orange-400 outline-none text-slate-500',
                                        'placeholder': 'e.g. DSA Example Test',
                                        'id': 'modal-email'}), label='Test Name: ', max_length=50,)

    instruction = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'e.g. Length of the test is one hour',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)


class EditTestForm(forms.Form):
    test_name = forms.CharField(widget=forms.TextInput
                                (attrs={'class': 'border-b-2 mb-4 text-[17px] hover:border-slate-500 focus:border-orange-400 outline-none text-slate-500',
                                        'placeholder': 'e.g. DSA Example Test',
                                        'id': 'modal-email'}), label='Test Name: ', max_length=50,)

    instruction = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'e.g. Length of the test is one hour',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)


class AddQuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'Enter question',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)

    questionIsCode = forms.BooleanField(required=False)

    op1 = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'Enter Option 1',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)

    op1IsCode = forms.BooleanField(required=False)

    op2 = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'Enter Option 2',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)

    op2IsCode = forms.BooleanField(required=False)

    op3 = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'Enter Option 3',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)

    op3IsCode = forms.BooleanField(required=False)

    op4 = forms.CharField(widget=forms.Textarea
                                  (attrs={'class': 'tinymce border-2 rounded-md focus:outline-orange-400 mb-4 text-[17px] p-4 outline-1 hover:border-slate-500 text-slate-500',
                                          'placeholder': 'Enter Option 4',
                                          'id': 'modal-email'}), label='Test Name: ', required=False)

    op4IsCode = forms.BooleanField(required=False)
    
    OPTIONS = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4'),
    ]

    correct_op = forms.ChoiceField(
        choices=OPTIONS,
        widget=forms.RadioSelect(attrs={'class': 'size-4'}),
    )

#     correct_op = forms.CharField(label='Correct Option', widget=forms.TextInput(
#         attrs={'min': 1, 'max': '4', 'type': 'number', 'class': 'form-control', 'id': 'floatingInput'}))
