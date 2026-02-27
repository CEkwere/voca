from django.contrib import admin
from .models import Question, Choice, Charism, CharismDimension, CharismScore

class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['text', 'capuchin', 'dominican', 'benedictine', 'carmelite', 'augustinian']
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'text', 'choice_count']
    search_fields = ['text']
    inlines = [ChoiceInline]
    
    def question_number(self, obj):
        # Get the question number based on its position in the list
        questions = Question.objects.all().order_by('id')
        for i, q in enumerate(questions, 1):
            if q.id == obj.id:
                return f"Q{i}"
        return "N/A"
    question_number.short_description = "Question #"
    
    def choice_count(self, obj):
        return obj.choice_set.count()
    choice_count.short_description = "# of Choices"

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_number', 'choice_text', 'question_with_number']
    list_filter = ['question']
    search_fields = ['text', 'question__text']
    
    def question_with_number(self, obj):
        questions = Question.objects.all().order_by('id')
        for i, q in enumerate(questions, 1):
            if q.id == obj.question.id:
                return f"Q{i}: {obj.question.text[:50]}..."
        return obj.question.text
    question_with_number.short_description = "Question"
    
    def choice_number(self, obj):
        choices = obj.question.choice_set.all().order_by('id')
        for i, c in enumerate(choices, 1):
            if c.id == obj.id:
                return f"Choice {i}"
        return "N/A"
    choice_number.short_description = "Choice #"
    
    def choice_text(self, obj):
        return obj.text
    choice_text.short_description = "Answer Text"

@admin.register(Charism)
class CharismAdmin(admin.ModelAdmin):
    list_display = ['name', 'values', 'color']
    fields = ['name', 'description', 'values', 'color', 'icon']

@admin.register(CharismDimension)
class CharismDimensionAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

@admin.register(CharismScore)
class CharismScoreAdmin(admin.ModelAdmin):
    list_display = ['charism', 'dimension', 'score']
    list_filter = ['charism', 'dimension']