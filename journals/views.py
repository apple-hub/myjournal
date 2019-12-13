from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Journal, Comment
from .forms import JournalForm, CommentForm

# Create your views here.
def index(request):
    journals = Journal.objects.filter(updated_datetime__lte=timezone.now()).order_by('updated_datetime')
    return render(request, 'journals/index.html', {'journals':journals})

def journal_detail(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    return render(request, 'journals/journal_detail.html', {'journal': journal})

@user_passes_test(lambda u: u.is_superuser)
def journal_new(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.author = request.user
            journal.save()
            return redirect('journal_detail', pk= journal.pk)
    else:
        form = JournalForm()
    return render(request, 'journals/journal_edit.html', {'form':form})

@user_passes_test(lambda u: u.is_superuser)
def journal_edit(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.author = request.user
            journal.save()
            return redirect('journal_detail', pk= journal.pk)

    else:
        form = JournalForm(instance=journal)
    return render(request, 'journals/journal_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def journal_draft_list(request):
    drafts = Journal.objects.filter(updated_datetime__isnull=True).order_by('created_datetime')
    return render(request, 'journals/journal_draft_list.html', {'drafts':drafts})

@user_passes_test(lambda u: u.is_superuser)
def journal_publish(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    journal.publish()
    return redirect('journal_detail', pk=pk)

@user_passes_test(lambda u: u.is_superuser)
def journal_remove(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    journal.delete()
    return redirect('/')

@login_required
def add_comment_to_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.journal = journal
            comment.save()
            return redirect('journal_detail', pk=journal.pk)
    else:
        form = CommentForm()
    return render(request, 'journals/add_comment_to_journal.html', {'form':form})

@user_passes_test(lambda u: u.is_superuser)
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('journal_detail', pk=comment.journal.pk)
