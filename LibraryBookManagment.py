class BookNode: # Node for singly linked list
    def __init__(self, BookID, BookTitle, AuthorName, Status):
        self.BookID = BookID
        self.BookTitle = BookTitle
        self.AuthorName = AuthorName
        self.Status = Status 
        self.next = None

class BookList: # Singly linked list to manage books
    def __init__(self):
        self.head = None
# Insert book at the end of the list
    def insertBook(self, BookID, BookTitle, AuthorName, Status="Available"):
        new_node = BookNode(BookID, BookTitle, AuthorName, Status)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
# Delete book by BookID
    def deleteBook(self, BookID):
        current = self.head
        prev = None
        while current:
            if current.BookID == BookID:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print("Book deleted successfully.")
                return True
            prev = current
            current = current.next
        print("Book not found.")
        return False
# Search book by BookID
    def searchBook(self, BookID):
        current = self.head
        while current:
            if current.BookID == BookID:
                print("book found:", current.BookTitle)
                return current
            current = current.next
        print("Book not found.")    
        return None
# Display all books
    def displayBooks(self):
        current = self.head
        if not current:
            print("No books in the library.")
        while current:
            print("BookID:", current.BookID, 
                  "\nTitle:", current.BookTitle,"\nAuthorName:", current.AuthorName,
                  "\nStatus:", current.Status, "\n-------------------")
            current = current.next

# Stack to manage transactions
class TransactionStack:
    def __init__(self):
        self.stack = []
# Push transaction onto stack
    def push(self, trans):
        self.stack.append(trans)
# Pop transaction from stack
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("No transactions to undo.")
            return None
# View all transactions
    def viewTransactions(self):
        if not self.stack:
            print("No transactions recorded.")
            return
        print("Recent Transactions:")
        for trans in reversed(self.stack):
            print(trans)
# Transaction Management System
class TransactionManagementSystem:
    def __init__(self):
        self.booklist = BookList()
        self.transStack = TransactionStack()
# Issue a book
    def issueBook(self, BookID):
        book = self.booklist.searchBook(BookID)
        if book and book.Status == "Available":
            book.Status = "Issued"
            self.transStack.push(f"Issue BookID: {BookID}")
            print("book issued:", book.BookTitle)
        elif book:
            print("Book is already issued.")
# Return a book
    def returnBook(self, BookID):
        book = self.booklist.searchBook(BookID)
        if book and book.Status == "Issued":
            book.Status = "Available"
            self.transStack.push(f"Return BookID: {BookID}")
            print("book returned:", book.BookTitle)
        elif book:
            print("Book is not issued.")
# Undo last transaction
    def undoTransaction(self):
        trans = self.transStack.pop()
        if trans:
            action, info = trans.split(' ', 1)
            BookID = int(info.split(":")[1])
            book = self.booklist.searchBook(BookID)
            if book:
                if action == "Issue":
                    book.Status = "Available"
                    print("Undo Issue: Book", BookID, "marked as Available.")
                elif action == "Return":
                    book.Status = "Issued"
                    print("Undo Return: Book", BookID, "marked as Issued.")
# View all transactions
    def viewTransactions(self):
        self.transStack.viewTransactions()


if __name__ == "__main__":
    tms = TransactionManagementSystem()
    tms.booklist.insertBook(101, "The Great Gatsby", "F. Scott Fitzgerald")
    tms.booklist.insertBook(102, "1984", "George Orwell")
    tms.booklist.insertBook(103, "The Alchemist", "Paulo Coelho")
    tms.booklist.searchBook(102)
    tms.booklist.displayBooks()
    tms.booklist.deleteBook(103)
    tms.booklist.displayBooks()
    tms.issueBook(101)
    tms.returnBook(101)
    tms.undoTransaction()
    tms.viewTransactions()
    tms.booklist.displayBooks()
